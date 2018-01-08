from flask import request
from flask_restplus import Resource, Namespace

# /Users/jakanakiwanuka/work/RestplusDemo/app/app/apis/models/user.py
from app.apis.models.user import User

api = Namespace('Users', description='User sign up and login operations')

@api.route('/register')
class UserRegistration(Resource):

    @api.response(201, 'User succesfully Registered')
    @api.response(409, 'Conflict, User already exists')
    def post(self):
        """Registers a user """
        pass

    def get(self):
        """get all registered users"""
        pass