from .. import db
from app.main.model.address import Address

def create_address(data):
    address = Address(**data)

    db.session.add(address)
    db.session.commit()

    return "Success Created"

def get_addresses():
    return Address.query.all()

def get_a_address(address_id):
    return Address.query.get(address_id)

def update_address(address_id, data):
    address = Address.query.filter(Address.id==address_id).one()
    address.first_name = data.get("first_name")

    db.session.add(address)
    db.session.commit()

def delete_address(address_id):
    address = Address.query.get(address_id)
    db.session.delete(address)
    db.session.commit()