from flask import Blueprint, jsonify, make_response
from flask_restplus import Api
# from .user import api as ns1
from .user import api as ns1

authorization = {
    'apiKey': {
        'type' : 'apiKey',
        'in' : 'header',
        'name': 'Authorization'
    }
}



apiv1_bp = Blueprint('apiv1', __name__)

api = Api(apiv1_bp,
    title='My RestPlus Yummy API documentation',
    version='1.0',
    description='An api to create, read, update and delete recipes',
    authorizations=authorization
)

from .category import api as ns2
from .recipie import api as ns3

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)