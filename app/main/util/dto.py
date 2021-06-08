
from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class CategoryDto:
    api = Namespace('category', description='category related')
    category = api.model('category', {
        'name':fields.String(required=True,  description='category')
    })

class ProductDto:
    api = Namespace('product', description='product related')
    product = api.model('product', {
        'title':fields.String(required=True, description='product title'),
        'barcode':fields.String(required=True, description='product barcode'),
        'model':fields.String(required=True, description='product model'),
        'stock':fields.Integer(required=True, description='product stock'),
        'sku':fields.String(required=True, description='product sku'),
        'list_price':fields.Float(required=True, description='product list_price'),
        'sale_price':fields.Float(required=True, description='product sale_price'),
        'description':fields.String(required=True, description='product description'),
        'currency':fields.String(required=True, description='product currency'),
        'status':fields.String(required=True, description='product status'),
        'tax':fields.Float(required=True, description='product tax'),

        'category_id':fields.Integer(required=True, description='product_category')
    })

class BrandDto:
    api = Namespace('brand', description='brand related')
    brand = api.model("brand", {
        'name':fields.String(required=True, description='brand name'),
        'is_active':fields.String(required=True, description='brand is_active')
    })

class AddressDto:
    api = Namespace('address', description='address related')
    address = api.model('address', {
        'first_name':fields.String(required=True, description='address first_name'),
        'last_name':fields.String(required=True, description='address last_name'),
        'city':fields.String(required=True, description='address city'),
        'country':fields.String(required=True, description='address country'),
        'zip_code':fields.String(required=True, description='address zip_code'),
        'street_address':fields.String(required=True, description='address street_address'),
        'phone_number':fields.String(required=True, description='address phone_number'),
        'user_id':fields.Integer(required=True, description='address user_id'),
    })