from flask import request
from flask_restplus import Resource, Namespace, fields

from app.models.category import Category
from .functionality.utilities import create_category

api = Namespace('category', description='Category related functionality')

category = api.model('category', {
    'category_id' : fields.Integer(readOnly=True, description='category unique identifier'),
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category'),
    'date_created' : fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified' : fields.DateTime(readOnly=True, description='Date modified'),
    'user_id' : fields.Integer(readOnly=True, description='Which User created this nanka')

})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

# category_list = api.inherit('Categories list', pagination, {
#     'items', fields.List(fields.Nested(category))
# })


@api.route('/create')
@api.response(201, 'Category successfully created.')
@api.response(409, 'Conflict, Category already exists')
@api.expect(category)
class CategoryCreation(Resource):
    def post(self):
        """ Creates a new Category """
        data = request.get_json()
        print(data)
        categoryName = data.get('category_name')
        categoryDesc = data.get('category_description')
        user_id = data.get('user_id')
        # user = User.query.filter_by(id = user_id).first()
        if Category.query.filter_by(
                    user_id=user_id,
                    category_name=categoryName).first() is not None:
                return {'message': 'Category already exists'}, 409
        new_cat = Category(categoryName, categoryDesc, user_id)
        new_cat.save()
        return {'message': 'Category successfully created'}, 201

@api.route('/list')
# @api.marshal_list_with(category_list)
class CategoryCollection(Resource):
    def get(self):
        """List all current categories"""
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
