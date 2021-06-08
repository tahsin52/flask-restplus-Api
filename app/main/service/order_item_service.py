from .. import db
from ..model.order_item import OrderItem


def get_order_items():
    return OrderItem.query.all()

def get_a_order_item(order_item_id):
    return OrderItem.query.get(order_item_id)

def create_order_item(data):
    order_item = OrderItem(**data)

    db.session.add(order_item)
    db.session.commit()


def delete_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    db.session.delete(order_item)
    db.session.commit()

def update_order_item(order_item_id, data):
    order_item = OrderItem.query.filter(OrderItem.id == order_item_id).one()

    order_item.name = data.get('name')
    order_item.slug = data.get('slug')
    order_item.price = data.get('price')
    order_item.quantity = data.get('quantity')

    db.session.add(order_item)
    db.session.commit()