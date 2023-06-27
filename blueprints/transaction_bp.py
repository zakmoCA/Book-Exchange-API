from flask import Blueprint, request
from models.transaction import Transaction, TransactionSchema
from models.book import Book, BookSchema
from models.user import User, UserSchema
from init import db

transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions') # prefix means we don't need to include 'transactions' in the routes

# GET all transactions
@transactions_bp.route('/')
def all_transactions():
    
    # select * from transactions;
    stmt = db.select(Transaction).order_by(Transaction.id)
    transactions = db.session.scalars(stmt).all()
    return TransactionSchema(many=True).dump(transactions), 200