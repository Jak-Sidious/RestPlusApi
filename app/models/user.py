# app/models/user.py
from flask_restplus import Namespace, Resource, fields
from flask_bcrypt import Bcrypt
from app import db
from app.models.category import Category
import jwt
from datetime import datetime, timedelta



class User(db.Model):
    """This class represnets the Users table."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True, default='sample@sample.com')
    categories = db.relationship("Category", backref = "users",
                    lazy = 'dynamic', cascade='all, delete-orphan')
    recipies = db.relationship("Recipie", backref="users",
                    lazy = 'dynamic', cascade='all, delete-orphan')


    def __init__(self, username, password, email):
        ''' Initialise the user with a username '''
        self.username = username
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.email = email

    def password_is_valid(self, password):
        """
        Checks the password againts it's hash to validate the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        """Method to save instances of the User class in the database"""
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User: {}>'.format(self.username)