# app/apis/functionality/utilities.py

from app.apis.models.user import User


from flask import jsonify

def register_user(data):
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, password=password)
        user.save()
    # else:pyth
        