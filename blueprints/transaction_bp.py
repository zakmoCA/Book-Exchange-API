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
    if transactions is None:
        return {"error": "Transaction does not exist"}, 404
    return TransactionSchema(many=True).dump(transactions), 200

#CREATE a new transaction (request a book)
@transactions_bp.route('/request', methods=['POST'])
def request_book():
    
    transaction_info = TransactionSchema().load(request.json)

    requester_id = transaction_info['requester_id']
    requested_book_id = transaction_info['requested_book_id']

    stmt = db.select(Book).filter_by(id=requested_book_id)
    book = db.session.scalar(stmt)
    if book is None:
        return {"error": "Book not found"}, 404
    
    transaction = Transaction(
        requester_id=requester_id,
        requested_book_id=requested_book_id
    )
    db.session.add(transaction)
    db.session.commit()
    return TransactionSchema().dump(transaction), 201
