from typing import Tuple, Dict

from flask import request
from flask_restx import Resource

from ..service.brand_service import *
from ..util.dto import BrandDto

api = BrandDto.api
_brand = BrandDto.brand

@api.route('/')
class BrandList(Resource):
    @api.doc('list_of_registered_brand')
    @api.marshal_list_with(_brand, envelope='data')
    def get(self):
        """List all registered brand"""
        return get_brand()

    @api.expect(_brand, validate=True)
    @api.response(201, 'Brand successfully created.')
    @api.doc('create a new brand')
    def post(self) -> Tuple[Dict[str,str], int]:
        try:
            data = request.json
            create_brand(data=data)
            response_object = {
            'Status': "Success",
            'Message': "Successfully Created",
            'Data': data
        }
            return response_object, 201
        except Exception as e:
            raise e


@api.route('/<brand_id>')
@api.param('brand_id', 'The Brand identifier')
@api.response(404, 'Brand not found.')
class Brand(Resource):
    @api.doc('get a brand')
    @api.marshal_with(_brand)
    def get(self, brand_id):
        """get a brand given its identifier"""
        brand = get_a_brand(brand_id)
        if not brand:
            api.abort(404)
        else:
            return brand

    @api.response(204, 'Brand successfully updated')
    def put(self, brand_id):
        try:
            data = request.json
            update_brand(brand_id, data)
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

    @api.response(204, 'Brand successfully deleted.')
    def delete(self, brand_id):

        return delete_brand(brand_id), 204
