from init import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_STATUSES = ['Requested', 'Accepted', 'Declined', 'Completed']

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    requested_book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    provided_book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    status = db.Column(db.String(30))

    requester = db.relationship('User', back_populates='requested_transactions', foreign_keys=[requester_id])
    provider = db.relationship('User', back_populates='provided_transactions', foreign_keys=[provider_id])
    requested_book = db.relationship('Book', back_populates='requested_transactions', foreign_keys=[requested_book_id])
    provided_book = db.relationship('Book', back_populates='provided_transactions', foreign_keys=[provided_book_id])

class TransactionSchema(ma.Schema):
    requester_id = fields.Integer(required=True)
    provider_id = fields.Integer(required=True)
    requested_book_id = fields.Integer(required=True)
    provided_book_id = fields.Integer(required=True)
    status = fields.String(required=True, validate=OneOf(VALID_STATUSES, error=f'Status must be one of: {VALID_STATUSES}'))

    class Meta:
        fields = ('id', 'requester_id', 'provider_id', 'requested_book_id', 'provided_book_id', 'status')
        ordered = True
