from flask import request
from flask_restplus import Resource, Namespace, fields, marshal, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
# from app.apis.functionality.functions import edit_category, category_list

from app import db
from app.models.user import User
from app.models.category import Category

api = Namespace('category', 
                description='Category related functionality',
                path='/category/')

edit_category = api.model('edit category', {
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category')
})

category_list = api.model('category', {
    'user_id' : fields.Integer(readOnly = True, description='User that made the category'),
    'category_id': fields.Integer(readOnly =True, description='Unique identifier for each category'),
    'category_name' : fields.String(required=True, description='category name'),
    'category_description' : fields.String(required=True, description='A description about the current category'),
    'date_created' : fields.DateTime(readOnly=True, description = 'Date created'),
    'date_modified' : fields.DateTime(readOnnly=True, description = 'date modified')
})

Q_Parser = reqparse.RequestParser(bundle_errors=True)
Q_Parser.add_argument('q', required=False,
                        help='search for word', location='args')
Q_Parser.add_argument('page', required=False, type=int,
                        help='Number of pages', location='args')
Q_Parser.add_argument('per_page', required=False, type=int,
                        help='categories per page', default=10, location='args')


@api.route('/list')

class CategoryCollection(Resource):
    @jwt_required
    @api.expect(Q_Parser)
    @api.response(404, 'This user has no categories')
    @api.response(200, 'Recipies found')
    def get(self):
        '''List all current categories'''

        user_identity = get_jwt_identity()
        # created = User.query.filter_by(user_id=user_identity).first()
        the_cat = Category.query.filter_by(user_id=user_identity)
        args = Q_Parser.parse_args(request)
        q = args.get('q', '')
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        if q:
            the_cat = Category.query.filter(
                                Category.category_name.like("%" + q + "%"))

            # for a_category in the_categories:
            
        paged_cats = the_cat.paginate(page, per_page, error_out=False)
        if not paged_cats.items:
            return {'message': 'This user has no categories'}, 404
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
        '''Creates a new Category '''
        data = request.get_json()
        categoryName = data.get('category_name')
        categoryDesc = data.get('category_description')
        user_id = get_jwt_identity()
        if Category.query.filter_by(
                    user_id=user_id,
                    category_name=categoryName).first() is not None:
                return {'message': 'Category already exists'}, 409
        new_cat = Category(categoryName, categoryDesc, user_id)
        new_cat.save()
        return {'category_id' : new_cat.category_id,
                'message': 'Category successfully created'}, 201


@api.route('/<int:category_id>')
@api.response(404, 'The Category you are querying does not exist.')
class CategoryItem(Resource):
    '''Functionality for the viewing, updating and deleting of a 
    particular category
    '''

    @api.response(200, 'Category found successfully')
    @api.marshal_list_with(category_list)
    @jwt_required
    def get(self, category_id):
        '''Returns a particular category'''
        user_id = get_jwt_identity()
        response = Category.query.filter_by(user_id=user_id, 
                                        category_id=category_id).first()
        if response is None:
            return {'message': 'The Category you are querying does not exist.'}, 404
        return marshal(response, category_list)
        

    @api.response(204, 'Category successfully updated.')
    @api.response(404, "No such category exists")
    @api.response(403, "Forbidden, You don't own this category")
    @jwt_required
    @api.expect(edit_category)
    def put(self, category_id):
        ''' Updates an existing category '''
        user_id = get_jwt_identity()
        edit_cat = Category.query.filter_by(user_id=user_id, category_id=category_id).first()
        if edit_cat is None:
            return {'message': 'No such category exists'}, 404
        data = request.get_json()
        edit_cat.category_name = data.get('category_name')
        edit_cat.category_description = data.get('category_description')
        db.session.add(edit_cat)
        db.session.commit()
        return {'message': 'Category successfully updated'}

    @api.response(204, 'Category successfully deleted.')
    @api.response(404, 'Not Found, Category does not exixt')
    @jwt_required
    def delete(self, category_id):
        '''Deletes an existing Category'''
        user_id = get_jwt_identity()
        the_cat = Category.query.filter_by(user_id=user_id, category_id=category_id).first()

        if the_cat is not None:
            db.session.delete(the_cat)
            db.session.commit()
            return {'message': 'Category successfully deleted.'}, 204
        return {'message' : 'Not Found, Category does not exixt'}, 404
