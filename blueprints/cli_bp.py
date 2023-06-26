from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.book import Book
from datetime import date

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@cli_bp.cli.command('seed')
def seed_db():
    users = [
        User(
        username='TestUser1',
        email='testuser1@spam.com',
        password=bcrypt.generate_password_hash('password').decode('utf-8')
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
        publication_year = 1996
        )
    ]

    # Truncate the Book table
    db.session.query(Book).delete()
    
    # Add the book to the session (transaction)
    db.session.add_all(books)
    
    # Commit the transaction to the database
    db.session.commit()

    print('Models seeded')