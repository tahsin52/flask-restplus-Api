from typing import Tuple, Dict

from flask import request
from flask_restx import Resource

from ..service.category_service import create_category, get_category, get_a_category, update_category, delete_category
from ..util.dto import CategoryDto

api = CategoryDto.api
_category = CategoryDto.category

@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_registered_category')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all registered users"""
        return get_category()

    @api.expect(_category, validate=True)
    @api.response(201, 'Category successfully created.')
    @api.doc('create a new category')
    def post(self) -> Tuple[Dict[str,str], int]:
        data = request.json
        return create_category(data=data)

@api.route('/<category_id>')
@api.param('category_id', 'The User identifier')
@api.response(404, 'User not found.')
class Category(Resource):
    @api.doc('get a category')
    @api.marshal_with(_category)
    def get(self, category_id):
        """get a category given its identifier"""
        category = get_a_category(category_id)
        if not category:
            api.abort(404)
        else:
            return category

    @api.response(204, 'Category successfully updated')
    def put(self, category_id):
        try:
            data = request.json
            update_category(category_id, data)
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

    @api.response(204, 'Category successfully deleted.')
    def delete(self, category_id):

        return delete_category(category_id), 204
