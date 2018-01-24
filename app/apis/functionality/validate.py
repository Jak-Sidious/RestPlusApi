#app/apis/functionality/validate.py

import re

def username_validate(username):
    '''validator to ensure that username input matches the string structure'''
    username_pattern = re.compile(r'^[a-zA-Z_]+([a-zA-Z0-9]{1,10})$')
    if username_pattern.match(username):
        return True
    return False

def password_validate(password):
    '''validate to ensure that username inout matches the string structure'''
    password_pattern = re.compile(r'^[a-zA-Z0-9]{6,25}$')
    if password_pattern.match(password):
        return True
    return False

def email_validate(email):
    '''validate email matches a certain pattern'''
    email_pattern = re.compile(r'(^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)')
    if email_pattern.match(email):
        return True
    return False

def name_validate(name):
    '''validate recipie and category names to ensure that they are not null'''
    name_pattern = re.compile(r'^[a-zA-Z\s]+')
    result = name_pattern.match(name)
    if result is None:
        return False
    result = result.group()
    if len(result) is len(name):
        return True
    return False
