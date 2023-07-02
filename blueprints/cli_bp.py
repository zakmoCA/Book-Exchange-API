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
        username='Admin',
        email='admin@test.com',
        password=bcrypt.generate_password_hash('adminpass').decode('utf-8'),
        location_id = melbourne.id,
        is_admin=True
        ),
        User(
        username='Clayton Bigsby',
        email='cbigsby@test.com',
        password=bcrypt.generate_password_hash('cbigsbypass').decode('utf-8'),
        location_id = melbourne.id
        ),
        User(
        username='Ashy Larry',
        email='alarry@test.com',
        password=bcrypt.generate_password_hash('alarrypass').decode('utf-8'),
        location_id = melbourne.id
        ),
        User(
        username='Silky Johnson',
        email='sjohnson@test.com',
        password=bcrypt.generate_password_hash('sjohnsonpass').decode('utf-8'),
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
        ),
        Book(
        title = 'Dominion',
        author = 'Tom Holland',
        genre = 'History',
        publication_year = 2019,
        owner_id = users[1].id
        ),
        Book(
        title = 'Energy and Civilization: A History',
        author = 'Vaclav Smil',
        genre = 'History',
        publication_year = 2017,
        owner_id = users[3].id
        ),
        Book(
        title = 'The Beginning of Infinity',
        author = 'David Deutsch',
        genre = 'Physics, Pop Science',
        publication_year = 2011,
        owner_id = users[2].id
        ),
        Book(
        title = 'This Is Goint to Hurt: Secret Diaries of a Junior Doctor',
        author = 'Adam Kay',
        genre = 'Memoir',
        publication_year = 2017,
        owner_id = users[3].id
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
        ),
        Transaction(
        requester_id = users[2].id,
        requested_book_id = books[2].id
        ),
        Transaction(
        requester_id = users[0].id,
        requested_book_id = books[2].id
        )
    ]

    db.session.query(Transaction).delete()
    db.session.add_all(transactions)
    db.session.commit()

    print('Models seeded')