from typing import Tuple, Dict

from flask import request
from flask_restx import Resource

from ..service.order_service import *
from ..util.dto import OrderDto

api = OrderDto.api
_order = OrderDto.orders

@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_registered_order')
    @api.marshal_list_with(_order, envelope='data')
    def get(self):
        return get_orders()


    @api.expect(_order, validate=True)
    @api.response(201, 'Order successfully created.')
    @api.doc('create a new order')
    def post(self) -> Tuple[Dict[str,str], int]:
        data = request.json
        return create_order(data=data)

