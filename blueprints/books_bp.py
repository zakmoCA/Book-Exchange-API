from flask import Blueprint, request
from models.book import Book, BookSchema
from models.user import User, UserSchema
from init import db

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

