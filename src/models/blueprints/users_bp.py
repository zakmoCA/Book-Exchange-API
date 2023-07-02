from flask import Blueprint, request
from models.user import User, UserSchema
from init import db


users_bp = Blueprint('users', __name__, url_prefix='/users') # prefix means we don't need to include 'users' in the routes


# GET all users
@users_bp.route('/')
def all_users():
    
    # select * from books;
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users), 200

# GET specific user
@users_bp.route('/<int:user_id>')
def one_book(user_id):
    
    # select * from books;
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user is None:
        return {"error": "User not found"}, 404
    return UserSchema().dump(user), 200

