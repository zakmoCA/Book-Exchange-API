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