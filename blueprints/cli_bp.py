from flask import Blueprint
from init import db
from models.user import User
from models.book import Book
from datetime import date

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')