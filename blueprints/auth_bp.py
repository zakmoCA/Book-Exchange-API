from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


 
auth_bp = Blueprint('auth', __name__, url_prefix='/auth') 

@auth_bp.route('/users')
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

#REGISTRATION
@auth_bp.route('/register', methods=['POST'])
def register():

    # Parse, sanitize and validate the incoming JSON data
    # via the schema
    user_info = UserSchema().load(request.json)
    # Create a new User model instance with the schema data
    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
        username=user_info['username'],
        location_id=user_info['location_id']
    )

    # Add and commit the new user
    db.session.add(user)
    db.session.commit()

    # Return the new user, excluding the password
    return UserSchema(exclude=['password']).dump(user), 201

#LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(days=10))
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email and password are required'}, 400
    
# DELETE user account
@auth_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_account(user_id):
    # Check if user is admin or the owner of the account
    if not admin_or_owner_required(user_id):
        return {"error": "Unauthorized"}, 401

    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user is None:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()

    return {"message": f"User account {user_id} deleted"}, 200

def admin_required():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401, description="You must be an admin") 

def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user and (user.is_admin or user_id == owner_id):
        return True
    else:
        return False
