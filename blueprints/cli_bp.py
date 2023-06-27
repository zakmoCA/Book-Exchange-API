from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.book import Book
from models.location import Location
from models.transaction import Transaction
from datetime import date

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@cli_bp.cli.command('seed')
def seed_db():
    melbourne = Location(
        city = 'Melbourne',
        state = 'VIC',
        country = 'Australia'
        )
    #commit and add to session
    db.session.add(melbourne)
    db.session.commit()

    
    users = [
        User(
        username='TestUser1',
        email='testuser1@spam.com',
        password=bcrypt.generate_password_hash('password').decode('utf-8'),
        location_id = melbourne.id
        ),
        User(
        username='TestUser2',
        email='testuser2@spam.com',
        password=bcrypt.generate_password_hash('password').decode('utf-8'),
        location_id = melbourne.id
        )
    ]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    books = [
        Book(
        title = 'Harry Potter',
        author = 'JK Rowling',
        genre = 'Fantasy',
        publication_year = 1996,
        owner_id = users[0].id
        )
    ]

    # Truncate the Book table
    db.session.query(Book).delete()
    
    # Add the book to the session (transaction)
    db.session.add_all(books)
    
    # Commit the transaction to the database
    db.session.commit()

    transactions = [
        Transaction(
        requester_id = users[1].id,
        requested_book_id = books[0].id
        )
    ]

    db.session.query(Transaction).delete()
    db.session.add_all(transactions)
    db.session.commit()

    print('Models seeded')