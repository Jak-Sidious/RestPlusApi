# app/apis/functionality/utilities.py

from app.models.user import User
from app.models.category import Category
from flask_jwt_extended import (
    jwt_required, create_access_token,get_jwt_identity
    )


from flask import jsonify

def register_user(data):
    '''Method to reguster a user'''
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, password=password)
        user.save()
    return {"message": "User succesfully registered"} , 201

        
def user_login(data):
    '''Method to enable a user to login'''
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None:
        return {"message": "User not registered"}, 404
    else:
        if user.password_is_valid(password):
            access_token = create_access_token(identity=user.user_id)
            return {"token": access_token}

def create_category(data, user_id):
    '''Method to to create a category'''
    cat_name = data.get('category_name')
    cat_desc = data.get('category_description')
    if Category.query.filter_by(user_id=user_id, category_name=
                                category_name).first() is not None:
                                return {"message": "Category already exists"}, 409
    new_cat = Category(cat_name, cat_desc, user_id)
    new_cat.save()
    return {"message": "Category successfully created"}, 201
