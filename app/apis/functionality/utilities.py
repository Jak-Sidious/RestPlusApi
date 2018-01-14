# app/apis/functionality/utilities.py

from app.models.user import User
# from sqlalchemy.orm.exc import NoResultFound


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
            access_token = user.generate_token(user.user_id)
            return access_token
    return access_token
