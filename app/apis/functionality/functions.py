from flask_restplus import Resource, Namespace, fields

from app import db
from app.models.user import User
from app.models.category import Category
from app.models.recipie import Recipie

# api = Namespace('users', description='User sign up and login operations')

# user_signup = api.model('user signup', {
#     'username' : fields.String(required=True, description='unique name for a user'),
#     'password' : fields.String(required=True, description='password required to grant a user access'),
#     'email' : fields.String(required=True, description='email required for a user')
# })

# user_login = api.model('users', {
#     'username' : fields.String(required=True, description='unique name for a user'),
#     'password' : fields.String(required=True, description='password required to grant a user access'),
# })