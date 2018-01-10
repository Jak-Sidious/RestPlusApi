#app/models/recipie.py

from flask_bcrypt import Bcrypt
from app import db
from app.apis.models.user import User
from app.apis.models.category import Category

import jwt
from datetime import datetime, timedelta

class Recipie(db.Model):
    """This class represents the recipies table"""

    __tablename__ = 'recipies'

    recipie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipie_name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False )
    attached_category = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    date_created = db.Column(db.DateTime(), default=datetime.now)
    date_modified = db.Column(db.DateTime(), default=datetime.now)

    def init(self, recipie_id, recipie_name, ingredients, created_by, attached_category):
        """ Initalise a recipie with a name, ingredients, created by 
        and attached category """
        self.recipie_name = recipie_name
        self.ingredients = ingredients
        self.attached_category = attached_category
        self.created_by = created_by

    def save(self):
        """Save a recipie"""
        # save a category
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        #  tells python how to print objects of a Recipie class
        return '<Recipie: {}>'.format(self.recipie_name)
