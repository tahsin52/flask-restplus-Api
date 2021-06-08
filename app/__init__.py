from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.category_controller import api as category_ns
from .main.controller.product_controller import api as product_ns
from .main.controller.brand_controller import api as brand_ns
from .main.controller.address_controller import api as address_ns


blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus (restx) web service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(category_ns, path='/category')
api.add_namespace(product_ns, path='/product')
api.add_namespace(brand_ns, path='/brand')
api.add_namespace(address_ns, path="/address")