from datetime import timedelta
from flask import request, json
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity, get_raw_jwt
    )

from app import db
from app.models.user import User
from app.models.blacklist import Blacklist
from .functionality.validate import (
    username_validate, password_validate, email_validate
    )                                   
    
api = Namespace('users', description='User sign up and login operations')

user_signup = api.model('user signup', {
    'username' : fields.String(required=True, description='unique name for a user'),
    'password' : fields.String(required=True, description='password required to grant a user access'),
    'email' : fields.String(required=True, description='email required for a user')
})

user_login = api.model('users', {
    'username' : fields.String(required=True, description='unique name for a user'),
    'password' : fields.String(required=True, description='password required to grant a user access'),
})

password_reset = api.model('password reset', {
    'old_password' : fields.String(required=True, description='existing user password'),
    'new_password' : fields.String(required=True, description='password to change to')
})


@api.route('/register')
class UserRegistration(Resource):

    @api.response(201, 'User succesfully Registered')
    @api.response(409, 'Conflict, User already exists')
    @api.expect(user_signup)
    def post(self):
        '''Registers a user '''
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        validated_username = username_validate(username)
        validated_password = password_validate(password)
        validated_email = email_validate(email)

        if validated_username is False:
            return {'message': 'Username is invalid it should contain' 
                    ' alphanumeric charcaters followed by an underscore'
                    ' of not more than 25 characters'}, 422

        if validated_password is False:
            return {'message': 'Password must be between 6 and 25 alphanumeric'
                    ' characters'}, 422
        
        if validated_email is False:
            return {'message': 'Email needs to be in the format ###@###.###'}, 422 
        # user = User.query.filter_by(username=username,
        #                             password=password,
        #                             email=email).first()
        if User.query.filter_by(username=username).first() is not None:
            return {"message": f"Username {username} already exists"}, 409
        if User.query.filter_by(email=email).first() is not None:
            return {"message": f"email {email} already exists"}, 409
        user = User(username=username, password=password, email=email)
        user.save()
                
        return {"message": "User succesfully registered"} , 201
            

@api.route('/login')
class UserLogin(Resource):
    @api.response(200, 'User sucessfully Loged in')
    @api.response(401, 'Invalid credentials, please try again')
    @api.response(404, 'The requested username is unavailable')
    @api.expect(user_login)
    def post(self):
        '''Logs in a regestered user'''
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        validated_username = username_validate(username)
        validated_password = password_validate(password)
        if validated_username is False:
            return {'message': 'Username is invalid it should contain' 
                    ' alphanumeric charcaters followed by an underscore'
                    ' of not more than 25 characters'}, 422

        if validated_password is False:
            return {'message': 'Password must be between 6 and 25 alphanumeric'
                    ' characters'}, 422
        user = User.query.filter_by(username=username).first()
        if user is None:
            return {"message": "The requested username is unavailable"}, 404
        else:
            if user.password_is_valid(password):
                expires = timedelta(days=10)
                access_token = create_access_token(identity=user.user_id, 
                                                    expires_delta=expires)
                return {"user": user.username,
                        "token": access_token,
                        "response": "User sucessfully Loged in"}, 200
            return {"message": "Invalid credentials, please try again"}, 401

@api.route('/logout')
class UserLogout(Resource):
    @api.response(200, 'You have been logged out')
    @jwt_required
    def delete(self):
        '''Enable a user to succesfully logout'''
        jti = get_raw_jwt()['jti']
        blacklister = Blacklist(jti)
        db.session.add(blacklister)
        db.session.commit()
        return {'message': 'You have been logged out'}, 200


@api.route('/resetpassword')
class PasswordReset(Resource):
    @api.response(200, 'Password reset successfully')
    @api.response(422, 'Incorect password, please try again')
    @jwt_required
    @api.expect(password_reset)
    def put(self):
        '''Enable a user to succesfully reset their psssword'''
        userId = get_jwt_identity()
        user = User.query.filter_by(user_id=userId).first()
        data = request.get_json()
        old_pass = data.get('old_password')
        if user.password_is_valid(old_pass):
            new_pass = data.get('new_password')
            user.password = new_pass
            db.session.add(user)
            db.session.commit()
            return {'new password set': user.password,
                    'message': 'Password reset successfully'}, 200
        return {'message': 'Incorect password, please try again'}, 422