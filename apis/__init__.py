from flask_restplus import Api

from .cats import api as ns1

api = Api(
    title='My title',
    version='1.0',
    description='A description of sorts'
)

api.add_namespace(ns1)