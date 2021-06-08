from .. import db
from app.main.model.product import Product

def create_product(data):
    product = Product(**data)
    db.session.add(product)
    db.session.commit()

    return "Success!! Product Created!!"


def get_product():
    return Product.query.all()


def get_a_product(product_id):
    return Product.query.get(product_id)

def update_product(product_id, data):
    product = Product.query.get(product_id)
    product.title = data.get('title')
    db.session.add(product)
    db.session.commit()

def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()

    return "Product Deleted"