from flask import request
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.category import Category
from app.apis.functionality.parsers import pagination_args
from app.apis.recipie import recipe


api = Namespace('category', description='Category related functionality')

category = api.model('category', {
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

category_list = api.inherit('Category list', pagination, {
    'items':fields.List(fields.Nested(category))
})

category_n_recipes = api.inherit('Category and associated recipies', category, {
    'recipes': fields.List(fields.Nested(recipe, required=True))
})

@api.route('/list')
class CategoryCollection(Resource):
    
    @api.marshal_list_with(category_list)
    @jwt_required
    def get(self):
        """List all current categories"""

        # args = pagination_args.parse_args(request)
        # query = args.get('q')
        # page = args.get('page', 1)
        # per_page = args.get('per_page', 10)

        # if query is None:
        #     category_query = Category.query
        # else:
        #     category_query = Category.query.filter(Categories.name.like("%"+query+"%"))

        # categories_page = category_query.paginate(page, per_page,
        #             error_out = False)
        
        # return categories_page

@api.route('/create')

@api.response(201, 'Category successfully created.')
@api.response(409, 'Conflict, Category already exists')
@api.expect(category)
class CategoryCreation(Resource):
    @jwt_required
    def post(self):
        """ Creates a new Category """
        data = request.get_json()
        print(data)
        categoryName = data.get('category_name')
        categoryDesc = data.get('category_description')
        user_id = get_jwt_identity()
        if Category.query.filter_by(
                    user_id=user_id,
                    category_name=categoryName).first() is not None:
                return {'message': 'Category already exists'}, 409
        new_cat = Category(categoryName, categoryDesc, user_id)
        new_cat.save()
        return {'message': 'Category successfully created'}, 201




@api.route('/<int:category_id>')
@api.response(404, 'The Category you are querying does not exist.')
class CategoryItem(Resource):
    @api.marshal_list_with(category_n_recipes)
    @jwt_required
    def get(self, category_id):
        """Returns a particular category"""
        # return Category.query.filter(Category.category_id=category_id).one()

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
