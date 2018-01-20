#app/models/recipie.py

from flask_bcrypt import Bcrypt
from app import db

import jwt
from datetime import datetime, timedelta

class Recipie(db.Model):
    '''This class represents the recipies table'''

    __tablename__ = 'recipies'

    recipie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipie_name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id')
                            , nullable = False )
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), 
                            nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow())
    date_modified = db.Column(db.DateTime(), default=datetime.utcnow())

    def init(self, recipie_id, recipie_name, ingredients, created_by):
        '''Initalise a recipie with a name, ingredients, created by 
        and attached category''' 
        self.recipie_name = recipie_name
        self.ingredients = ingredients
        self.category_id = category_id
        self.created_by = created_by

    def save(self):
        '''Save a recipie'''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        '''tells python how to print objects of a Recipie class'''
        return '<Recipie: {} {} {} {}>'.format(self.recipie_name, self.ingredients, self.created_by, self.category_id)
