from typing import Tuple, Dict, Union, Any

from flask import request
from flask_restx import Resource

from ..service.product_service import get_product, create_product, get_a_product, update_product, delete_product
from ..util.dto import ProductDto

api = ProductDto.api
_product = ProductDto.product


@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_registered_product')
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """List all registered product"""
        return get_product()

    @api.expect(_product, validate=True)
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new product')
    def post(self) -> tuple[dict[str, Union[str, Any]], int]:
        try:
            data = request.json
            create_product(data=data)
            response_object = {
            'Status': "Success",
            'Message': "Successfully Created",
            'Data': data
        }
            return response_object, 201
        except Exception as e:
            raise e

@api.route('/<product_id>')
@api.param('product_id', 'The Product identifier')
@api.response(404, 'Product not found.')
class Category(Resource):
    @api.doc('get a product')
    @api.marshal_with(_product)
    def get(self, product_id):
        """get a product given its identifier"""
        category = get_a_product(product_id)
        if not category:
            api.abort(404)
        else:
            return category

    @api.response(204, 'Category successfully updated')
    def put(self, product_id):
        try:
            data = request.json
            update_product(product_id, data)
            response_object = {
                'Status': "Success",
                'Message': "Successfully Updated",
                'Data': data
            }
            return response_object
        except Exception as e:
            response_object = {
                'Status': "Fail",
                'Message': str(e),
            }
            return response_object

    @api.response(204, 'Product successfully deleted.')
    def delete(self, product_id):

        return delete_product(product_id), 204
