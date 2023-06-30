from flask import Blueprint, request
from models.book import Book, BookSchema
from models.user import User
from init import db
from sqlalchemy import or_
from blueprints.auth_bp import admin_required, admin_or_owner_required
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError

books_bp = Blueprint('books', __name__, url_prefix='/books') # prefix means we don't need to include 'books' in the routes

# GET all books
@books_bp.route('/')
def all_books():
    
    # select * from books;
    stmt = db.select(Book).order_by(Book.title.desc())
    books = db.session.scalars(stmt).all()
    return BookSchema(many=True).dump(books), 200

# GET 1 book
@books_bp.route('/<int:book_id>')
def one_book(book_id):
    
    # select * from books;
    stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(stmt)
    if book is None:
        return {"error": "Book not found"}, 404
    return BookSchema().dump(book), 200


# SEARCH for a book via title (author next?)
@books_bp.route('/search', methods=['GET'])
def search_books():
    search_query = request.args.get('query')
  
    # using SQLAlchemy's ilike function for case insensitive search
    stmt = db.select(Book).filter(
        or_(# or_ is used to create a SQL query that will match either title or author
            Book.title.ilike(f"%{search_query}%"), # THINK ABOUT SETTING LOWER BOUNDS FOR LENGTH OF SEARCH QUERY
            Book.author.ilike(f"%{search_query}")
        ))
    print(stmt)
    books = db.session.scalars(stmt).all()
    return BookSchema(many=True).dump(books), 200

# GET all books at specific location
@books_bp.route('/location/<int:location_id>', methods=['GET'])
def get_books_by_location(location_id):
    stmt = db.select(Book).join(User).filter(User.location_id == location_id)# using SQLAlchemy's join function to join users and books based on location
    books = db.session.scalars(stmt).all()
    return BookSchema(many=True).dump(books), 200

# ADD a book
@books_bp.route('/', methods=['POST'])
@jwt_required()  
def add_book():
    user_id = get_jwt_identity()  # Gets the ID of the currently authenticated user from the JWT

    admin_or_owner_required(user_id)
    
    book_info = BookSchema().load(request.json)  # Loads the JSON data from the request into the BookSchema
    
    book_info['owner_id'] = user_id  # Sets the owner_id field of the book to be the ID of the currently authenticated user
    book = Book(**book_info)  # Creates a new Book object with the data loaded from the request
    db.session.add(book)  # Adds the new book to the database session
    try:
        db.session.commit() 
    except IntegrityError:  # This exception is raised if there is a conflict, such as trying to add a book with a title that already exists in the database
        db.session.rollback()  # If there is a conflict, the changes are rolled back
        return {"error": "A book with this information already exists"}, 400  # An error message is returned with a 400 Bad Request status code
    return BookSchema().dump(book), 201  # If there is no conflict, the new book is returned in the response, along with a 201 Created status code

# DELETE a book
@books_bp.route('/<int:book_id>', methods=['DELETE'])
@jwt_required()  
def delete_book(book_id):  # Passing book_id to the function automatically as it is part of URL
    user_id = get_jwt_identity()  # Gets the ID of the currently authenticated user from the JWT
    admin_or_owner_required(user_id)
    book = Book.query.get_or_404(book_id)  # Retrieves the book with the given ID from the database, or returns a 404 not found code if it doesn't exist
    if book.owner_id != user_id:  # If the ID of the book's owner is not the same as the ID of the currently authenticated user
        return {"error": "You do not have permission to delete this book"}, 403  # an error message is returned with a 403 Forbidden status code
    db.session.delete(book)  # The book is deleted from the database session
    db.session.commit()  # The changes are committed to the database
    return {"message": "Book deleted"}, 204  # Success message is returned with a 204 No Content status code


# UPDATE a book
@books_bp.route('/<int:book_id>', methods=['PUT'])
@jwt_required() 
def update_book(book_id):  # Passing book_id to the function automatically as it is part of URL
    user_id = get_jwt_identity()  # Gets the ID of the currently authenticated user from the JWT
    book = Book.query.get_or_404(book_id)  # Retrieves the book with the given ID from the database, or returns a 404 not found code if it doesn't exist
    # Check if the user is an admin or the owner of the book
    if not admin_or_owner_required(user_id, book.owner_id):
        return {"error": "You do not have permission to update this book"}, 403  # an error message is returned with a 403 Forbidden status code
    book_info = BookSchema().load(request.json)  # Loads the JSON data from the request into the BookSchema
    for key, value in book_info.items():  # This loop goes through each field in the loaded data
        setattr(book, key, value)  # The corresponding attribute of the book is updated with the new value
    db.session.commit()  # The changes are committed to the database
    return BookSchema().dump(book), 200  # The updated book is returned in the response, along with a 200 OK status code  

