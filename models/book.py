from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(100), nullable=True)
    publication_year = db.Column(db.Integer, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    owner = db.relationship('User', back_populates='user_books')
    requested_transactions = db.relationship('Transaction', back_populates='requested_book', foreign_keys='Transaction.requested_book_id', cascade='delete')
    provided_transactions = db.relationship('Transaction', back_populates='provided_book', foreign_keys='Transaction.provided_book_id', cascade='delete')



class BookSchema(ma.Schema):
    title = fields.String(required=True, validate=Length(min=1, max=200, error='Title must be between 1 and 200 characters long'))
    author = fields.String(required=True, validate=Length(min=1, max=100, error='Author name must be between 1 and 100 characters long'))
    genre = fields.String(validate=Length(max=100, error='Genre must be up to 100 characters long'))
    publication_year = fields.Integer()

    class Meta:
        fields = ('id', 'title', 'author', 'genre', 'publication_year', 'owner_id')
        ordered = True
