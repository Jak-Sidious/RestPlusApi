# app/apis/functionality/serializers.py
from flask_restplus import fields, Resource

from app.apis import api
# /Users/jakanakiwanuka/work/RestplusDemo/app/app/apis/__init__.py

"""This file deals with data validation"""

recipe = api.model('recipie', {
    'recipie_id' : fields.Integer(readOnly=True, description='recipie unique identifier'),
    'recipie_name' : fields.String(required=True, description='recipie name'),
    'ingedients' : fields.String(required=True, description='A description of the ingredients to compile the recipie'),
    'created_by' : fields.Integer(readOnly=True, description='Which User created this nanka'),
    'attached_category' : fields.Integer(readOnly=True, description='Which category does this recipe belong to'),
    'date_created' : fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified' : fields.DateTime(readOnly=True, description='Date modified')
})


category = api.model('category', {
    'category_id' : fields.Integer(readOnly=True, description='category unique identifier'),
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category'),
    'date_created' : fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified' : fields.DateTime(readOnly=True, description='Date modified'),
    'created_by' : fields.Integer(readOnly=True, description='Which User created this nanka')
})

usah = api.model('users', {
    'username' : fields.String(required=True, description='unique name for a user'),
    'password' : fields.String(required=True, description='password required to grant a user access')
})


