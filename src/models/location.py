from src.init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))

    users = db.relationship('User', back_populates='location')

class LocationSchema(ma.Schema):
    city = fields.String(required=True, validate=Length(min=1, max=100))
    state = fields.String(required=True, validate=Length(min=1, max=100))
    country = fields.String(required=True, validate=Length(min=1, max=100))
 
    class Meta:
        fields = ('id', 'city', 'state', 'country')
        ordered = True

