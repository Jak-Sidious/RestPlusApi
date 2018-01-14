from flask import request
from flask_restplus import Resource, Namespace, fields

from app.models.recipie import Recipie
# from ..functionality.serializers import recipe

api = Namespace('recipie', description='Recipie related functionality')

recipe = api.model('recipie', {
    'recipie_id' : fields.Integer(readOnly=True, description='recipie unique identifier'),
    'recipie_name' : fields.String(required=True, description='recipie name'),
    'ingedients' : fields.String(required=True, description='A description of the ingredients to compile the recipie'),
    'created_by' : fields.Integer(readOnly=True, description='Which User created this nanka'),
    'attached_category' : fields.Integer(readOnly=True, description='Which category does this recipe belong to'),
    'date_created' : fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified' : fields.DateTime(readOnly=True, description='Date modified')
})


@api.route('/')
class RecipieCollection(Resource):
    def get(self):
        """Returns a list of Recipies"""
        pass

    @api.response(201, 'Category successfully created.')
    @api.response(409, 'Conflict, Category already exists')
    @api.expect(recipe)
    def post(self):
        """ Creates a new Recipie """
        pass

# @api.route('/<int:category_id>')
# @api.response(404, 'The Category you are querying does not exist.')
# class CategoryItem(Resource):
#     def get(self, category_id):
#         """Returns a particular category"""
#         pass

#     @api.response(204, 'Category successfully updated.')
#     @api.response(404, "Not Found, Category doesn't exist")
#     @api.response(403, "Forbidden, You don't own this category")
#     def put(self, category_id):
#         """ Updates an existing category """
#         pass

#     @api.response(204, 'Category successfully deleted.')
#     @api.response(404, 'Not Found, Category does not exixt')
#     @api.response(403, "Forbidden, You don't own this category")
#     def delete(self, category_id):
#         """Deletes an existing Category"""
#         pass
