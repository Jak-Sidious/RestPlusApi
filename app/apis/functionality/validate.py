#app/apis/functionality/validate.py

import re

def username_validate(username):
    '''validator to ensure that username input matches the string structure'''
    username_pattern = re.compile(r'^[a-zA-Z_]+([a-zA-Z0-9]{1,10})$')
    if username_pattern.match(username):
        return True
    return False