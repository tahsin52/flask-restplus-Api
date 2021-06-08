from sqlalchemy.orm import relationship

from .. import db
from datetime import datetime


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    street_address = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=True)  # nullable because I have not implemented it

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='addresses')

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)