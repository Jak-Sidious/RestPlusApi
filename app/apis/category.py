from flask import request
from flask_restplus import Resource, Namespace, fields, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.models.user import User
from app.models.category import Category
from app.apis.functionality.parsers import pagination_args
from app.apis.recipie import recipe



api = Namespace('category', description='Category related functionality')

edit_category = api.model('edit category', {
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category')
})

category_list = api.model('category', {
    'category_id': fields.Integer(readOnly =True, description='Unique identifier for each category'),
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category'),
    'date_created' : fields.DateTime(readOnly=True, description = 'Date created'),
    'date_modified' : fields.DateTime(readOnnly=True, description = 'date modified'),
    'user_id' : fields.Integer(readOnly = True, description='User that made the category')
})

category_n_recipes = api.inherit('Category and associated recipies', category_list, {
    'recipes': fields.List(fields.Nested(recipe, required=True))
})

@api.route('/list')
class CategoryCollection(Resource):
    
    @api.marshal_list_with(category_list)
    @jwt_required
    def get(self):
        """List all current categories"""

        user_identity = get_jwt_identity()
        # create basse query object for pagination functionality
        created = User.query.filter_by(user_id=user_identity).first()
        user_cats = created.categories
        paged_cats = user_cats.paginate(error_out=False)
        paginated=[]
        for a_category in paged_cats.items:
            paginated.append(a_category)

        return marshal(paginated, category_list)


@api.route('/create')
class CategoryCreation(Resource):
    @jwt_required
    @api.response(201, 'Category successfully created.')
    @api.response(409, 'Conflict, Category already exists')
    @api.expect(edit_category)
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
    '''Functionality for the viewing, updating and deleting of a 
    particular category
    '''

    @api.response(200, 'Category found successfully')
    @api.marshal_list_with(category_n_recipes)
    @jwt_required
    def get(self, category_id):
        """Returns a particular category"""
        response = Category.query.filter_by(category_id=category_id).first()
        if response is None:
            return {'message': 'The Category you are querying does not exist.'}, 404
        return marshal(response, category_n_recipes)
        

    @api.response(204, 'Category successfully updated.')
    @api.response(404, "Not Found, Category doesn't exist")
    @api.response(403, "Forbidden, You don't own this category")
    @jwt_required
    @api.expect(edit_category)
    def put(self, category_id):
        """ Updates an existing category """
        pass

    @api.response(204, 'Category successfully deleted.')
    @api.response(404, 'Not Found, Category does not exixt')
    @api.response(403, "Forbidden, You don't own this category")
    @jwt_required
    def delete(self, category_id):
        """Deletes an existing Category"""
        the_cat = Category.query.filter_by(category_id=category_id).first()
        print (the_cat)

        if the_cat is not None:
            db.session.delete(the_cat)
            db.session.commit()
            return {'message': 'Category successfully deleted.'}, 204
        return {'message' : 'Not Found, Category does not exixt'}, 404
