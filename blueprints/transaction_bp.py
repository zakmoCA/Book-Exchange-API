from flask import Blueprint, request
from models.transaction import Transaction, TransactionSchema
from models.book import Book, BookSchema
from models.user import User, UserSchema
from init import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_or_owner_required


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

# GET all transactions for the logged-in user
@transactions_bp.route('/user')
@jwt_required()
def user_transactions():
    # Get the logged-in user's id
    user_id = get_jwt_identity()
    # Run the admin or owner required function
    admin_or_owner_required(user_id)
    
    # Select all transactions where the requester_id is the user's id
    stmt = db.select(Transaction).where(Transaction.requester_id == user_id).order_by(Transaction.id)
    transactions = db.session.scalars(stmt).all()

    if transactions is None:
        return {"error": "No transactions found for this user"}, 404
    return TransactionSchema(many=True).dump(transactions), 200


#CREATE a new transaction (request a book)
@transactions_bp.route('/request', methods=['POST'])
@jwt_required()
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

# ACCEPT a request
@transactions_bp.route('/accept/<int:transaction_id>', methods=['PUT'])
@jwt_required()
def accept_request(transaction_id):
    # Get the logged-in user's id
    user_id = get_jwt_identity()
    # Retrieve the transaction with the given ID, or 404 if it doesn't exist
    transaction = Transaction.query.get_or_404(transaction_id)
    # Check if the user is the owner of the requested book
    if transaction.requested_book.owner_id != user_id:
        return {"error": "You do not have permission to accept this request"}, 403
    # Set the status of the transaction to 'Accepted'
    transaction.status = 'Accepted'
    transaction.provider_id = user_id
    transaction.provided_book_id = transaction.requested_book_id
    db.session.commit()  # Commit the change to the database
    return TransactionSchema().dump(transaction), 200  # Return the updated transaction
