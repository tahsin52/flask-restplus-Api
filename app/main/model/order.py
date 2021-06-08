from datetime import datetime

from sqlalchemy.orm import relationship

from .. import db

ORDER_STATUS = ['processed', 'delivered', 'in transit', 'shipped']

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_number = db.Column(db.String(155), unique=True)
    cargo_pag = db.Column(db.String(155))
    payment_type = db.Column(db.Integer)
    payment_status = db.Column(db.Integer)
    coupon = db.Column(db.String(155), unique=True)
    subtotal = db.Column(db.Float)
    grandtotal = db.Column(db.Float)

    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    address = relationship('Address', backref='orders', lazy=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='orders')

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return "<Order '{}'>".format(self.order_number)


