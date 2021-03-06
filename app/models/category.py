#app/models/category.py

from flask_bcrypt import Bcrypt
from app import db

from app.models.recipie import Recipie

import jwt
from datetime import datetime, timedelta

class Category(db.Model):
    '''This class represents the category table'''

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(50), nullable=False, unique=True)
    category_description = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    date_modified = db.Column(
        db.DateTime, default=datetime.utcnow(),
        onupdate=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipies = db.relationship("Recipie", backref = "categories",
                    lazy = 'dynamic',cascade='all, delete-orphan')


    def __init__(self, category_name, category_description, created_by):
        self.category_name = category_name
        self.category_description = category_description
        self.user_id = created_by

    def save(self):
        '''Method to save category instance'''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        '''tells python how to print objects of a class'''
        return '<Category name: {}>'.format(self.category_name)


    def delete(self):
        '''Delete an instance of the category class'''
        db.session.delete(self)
        db.session.commit()
