from flask import request
from flask_restplus import Resource, Namespace

# /Users/jakanakiwanuka/work/RestplusDemo/app/app/apis/models/user.py
from app.apis.models.user import User
from ..functionality.serializers import usah

api = Namespace('users', description='User sign up and login operations')

@api.route('/register')
class UserRegistration(Resource):

    @api.response(201, 'User succesfully Registered')
    @api.response(409, 'Conflict, User already exists')
    @api.expect(usah)
    def post(self):
        """Registers a user """
        pass


@api.route('/login')
class UserLogin(Resource):
    @api.response(200, 'User sucessfully Loged in')
    @api.response(404, 'User not registered')
    def post(self):
        """Logs in a regestered user"""
        pass
    
@api.route('/logout')
class UserLogout(Resource):
    @api.response(200, "Successfully loged out")
    def delete(self):
        """logout a regestered user"""
        pass
    