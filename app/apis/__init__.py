from flask_restplus import Api

from .models.cats import api as ns1
from .views.user import api as ns2

api = Api(
    title='My title',
    version='1.0',
    description='A description of sorts'
)

api.add_namespace(ns1)
api.add_namespace(ns2)