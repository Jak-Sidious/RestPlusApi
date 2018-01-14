from flask import request, json
from flask_restplus import Resource, Namespace, fields

# /Users/jakanakiwanuka/work/RestplusDemo/app/app/apis/models/user.py
from app.models.user import User
# from .functionality.serializers import usah
from .functionality.utilities import register_user, user_login

api = Namespace('users', description='User sign up and login operations')

usah = api.model('users', {
    'username' : fields.String(required=True, description='unique name for a user'),
    'password' : fields.String(required=True, description='password required to grant a user access')
})

@api.route('/register')
class UserRegistration(Resource):

    @api.response(201, 'User succesfully Registered')
    @api.response(409, 'Conflict, User already exists')
    @api.expect(usah)
    def post(self):
        """Registers a user """
        data = request.get_json()
        # 
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, password=password)
            user.save()
            return {"message": "User succesfully registered"} , 201
        else:
            return {"message": "User already exists"}, 409


@api.route('/login')
class UserLogin(Resource):
    @api.response(200, 'User sucessfully Loged in')
    @api.response(404, 'User not registered')
    @api.expect(usah)
    def post(self):
        """Logs in a regestered user"""
        data = request.get_json()
        user_login(data)
        return {"message": "User succesfully Loged in"}, 200
    