from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Email

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)

    books = db.relationship('Book', backref='owner', lazy='dynamic')
    transactions = db.relationship('Transaction', backref='user', lazy='dynamic')

class UserSchema(ma.Schema):
    username = fields.String(required=True, validate=Length(min=3, max=100, error='Username must be between 3 and 100 characters long'))
    email = fields.Email(required=True, validate=Email(error='Invalid email address'))
    password = fields.String(load_only=True, required=True, validate=Length(min=6, error='Password must be at least 6 characters long'))

    class Meta:
        fields = ('id', 'username', 'email', 'location_id')
        ordered = True

