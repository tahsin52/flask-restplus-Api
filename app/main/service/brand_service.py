import json

from .. import db
from app.main.model.brand import Brand


def create_brand(data):
    brand = Brand(**data)

    db.session.add(brand)
    db.session.commit()

    return "Success!! Data Created"

def get_brand():
    return Brand.query.all()

def get_a_brand(brand_id):
    return Brand.query.filter(Brand.id==brand_id).one_or_none()

def delete_brand(brand_id):
    brand = Brand.query.get(brand_id)
    db.session.delete(brand)
    db.session.commit()

    return "Success deleted"

def update_brand(brand_id, data):
    brand = Brand.query.filter(Brand.id == brand_id).one()
    brand.name = data.get('name')
    brand.is_active = data.get('is_active')

    db.session.add(brand)
    db.session.commit()
    return "Success Updated"