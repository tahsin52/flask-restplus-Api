from datetime import datetime

from sqlalchemy.orm import relationship

from .. import db

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, nullable=False)
    slug = db.Column(db.String)
    price = db.Column(db.Integer, index=True, nullable=False)
    quantity = db.Column(db.Integer, index=True, nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    order = relationship('Order', backref='order_items')

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = relationship('Product', backref='order_items')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='products_bought')

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def get_summary(self):
        return {
            'name': self.name, 'slug': self.slug,
            'product_id': self.product_id,
            'price': self.price, 'quantity': self.quantity
        }