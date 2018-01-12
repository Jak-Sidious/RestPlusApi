# app/models/user.py
from flask_restplus import Namespace, Resource, fields
from flask_bcrypt import Bcrypt
from app import db

import jwt
from datetime import datetime, timedelta


class User(db.Model):
    """This class represnets the Users table."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    #todo modify user model to incorporate more unique identifiers 
    def __init__(self, username, password):
        ''' Initialise the user with a username '''
        self.username = username
        self.password = Bcrypt().generate_password_hash(password).decode()

    # def password_hasher(self, password):
    #     ''' hashes the password '''
    #     self.password = Bcrypt().generate_password_hash(password).decode('utf-8')

    # def password_checker(self, password):
    #     ''' check if hashed password and password match '''
    #     return Bcrypt().check_password_hash(self.password, password)

    def password_is_valid(self, password):
        """
        Checks the password againts it's hash to validate the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        """Method to save instances of the User class in the database"""
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        """Generates the access token"""

        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(days=30),
                'iat': datettime.utcnow(),
                'sub': user_id
            }
            #create the byte string token using payload and secret key
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm = 'HS256'
            )
            return jwt_string
        except Exception as e:
            # return n error in tring format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # The token is expired return an error string
            return "Expired token, Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"

    def __repr__(self):
        return '<User: {}'.format(self.username)