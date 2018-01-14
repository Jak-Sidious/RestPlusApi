from flask import request
from flask_restplus import Resource, Namespace, fields

from app.models.category import Category
# from ..functionality.serializers import category

api = Namespace('category', description='Category related functionality')

category = api.model('category', {
    'category_id' : fields.Integer(readOnly=True, description='category unique identifier'),
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category'),
    'date_created' : fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified' : fields.DateTime(readOnly=True, description='Date modified'),
    'created_by' : fields.Integer(readOnly=True, description='Which User created this nanka')
})


@api.route('/')
class CategoryCollection(Resource):
    def get(self):
        """Returns a list of categories"""
        pass

    @api.response(201, 'Category successfully created.')
    @api.response(409, 'Conflict, Category already exists')
    @api.expect(category)
    def post(self):
        """ Creates a new Category """
        pass

@api.route('/<int:category_id>')
@api.response(404, 'The Category you are querying does not exist.')
class CategoryItem(Resource):
    def get(self, category_id):
        """Returns a particular category"""
        pass

    @api.response(204, 'Category successfully updated.')
    @api.response(404, "Not Found, Category doesn't exist")
    @api.response(403, "Forbidden, You don't own this category")
    def put(self, category_id):
        """ Updates an existing category """
        pass

    @api.response(204, 'Category successfully deleted.')
    @api.response(404, 'Not Found, Category does not exixt')
    @api.response(403, "Forbidden, You don't own this category")
    def delete(self, category_id):
        """Deletes an existing Category"""
        pass
