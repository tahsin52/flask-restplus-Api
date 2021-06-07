import json

from .. import db
from app.main.model.category import Category


def create_category(data):
    category = Category(**data)

    db.session.add(category)
    db.session.commit()

    return "Success!! Data Created"

def get_category():
    return Category.query.all()

def get_a_category(category_id):
    return Category.query.filter(Category.id==category_id).one_or_none()

def delete_category(category_id):
    category = Category.query.get(category_id)
    db.session.delete(category)
    db.session.commit()

    return "Success deleted"

def update_category(category_id, data):
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()
    return "Success Updated"