from flask import jsonify
from sqlalchemy import desc

from app.main import db
from app.main.model.order import Order


def get_orders():
    orders = Order.query.all().order_by(desc(Order.created_at))

    return jsonify(orders)

def get_a_order(order_id):
    order = Order.query.get(order_id)

    return jsonify(order)

def create_order(data):
    order = Order(**data)

    db.session.add(order)
    db.session.commit()

    return "Success Created"

def update_order(order_id, data):
    order = Order.query.filter(Order.id == order_id).one()
    order.order_number = data.get('order_number')
    order.cargo_pag = data.get('cargo_pag')
    order.payment_type = data.get('payment_type')
    order.payment_status = data.get('payment_status')
    order.coupon = data.get('coupon')
    order.subtotal = data.get('subtotal')
    order.grandtotal = data.get('grandtotal')
    order.address_id = data.get('address_id')


    db.session.add(order)
    db.session.commit()

def delete_order(order_id):
    order = Order.query.get(order_id)


    db.session.delete(order)
    db.session.commit()
