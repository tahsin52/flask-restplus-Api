from typing import Dict, Tuple, Union

from flask_restx import errors

from .. import db
from app.main.model.product import Product


def create_product(data: Dict[str, str]) -> Union[Product, tuple[dict[str, str], int]]:
    product = Product.query.filter_by(title=data['title']).first()
    if not product:
        new_product = Product(
            title=data.get('title'),
            barcode=data.get('barcode'),
            model=data.get('model'),
            stock=data.get('stock'),
            sku=data.get('sku'),
            list_price=data.get('list_price'),
            sale_price=data.get('sale_price'),
            description=data.get('description'),
            currency=data.get('currency'),
            status=data.get('status'),
            tax=data.get('tax'),
            category_id=data.get('category_id'),
            brand_id=data.get('brand_id'),
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists. Please Log in.',
        }
        return response_object, 409

def get_product():
    return Product.query.all()



def get_a_product(product_id):
    return Product.query.get(product_id)

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if product:
        product.title = data.get('title')
        product.model = data.get('model')
        product.barcode = data.get('barcode')
        product.stock = data.get('stock')
        product.sku = data.get('sku')
        product.list_price = data.get('list_price')
        product.sale_price = data.get('sale_price')
        product.description = data.get('description')
        product.currency = data.get('currency')
        product.tax = data.get('tax')
        product.category_id = data.get('category_id')
        product.brand_id = data.get('brand_id')
    else:
        errors.abort(404, 'Product Not Found')

    db.session.add(product)
    db.session.commit()

def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()

    return "Product Deleted"