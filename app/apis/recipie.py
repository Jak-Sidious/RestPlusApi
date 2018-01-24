from flask import request
from flask_restplus import Resource, Namespace, fields, marshal, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.user import User
from app.models.recipie import Recipie

from app.models.category import Category

api = Namespace('recipie',
                description='Recipie related functionality',
                path='/recipes/')

recipe = api.model('recipie', {
    'recipie_id': fields.Integer(readOnly=True, description='recipie unique identifier'),
    'recipie_name': fields.String(required=True, description='recipie name'),
    'ingredients': fields.String(required=True, description='A description of the ingredients to compile the recipie'),
    'created_by': fields.Integer(readOnly=True, description='Which User created this nanka'),
    'category_id': fields.Integer(readOnly=True, description='Which category does this recipe belong to'),
    'date_created': fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified': fields.DateTime(readOnly=True, description='Date modified')
})


recipie_data = api.model('create recipie', {
    'recipie_name': fields.String(required=True, description='Name of the current recipe'),
    'ingredients': fields.String(required=True, description='The ingredients for this recipie')
})


Q_Parser = reqparse.RequestParser(bundle_errors=True)
Q_Parser.add_argument('q', required=False,
                        help='search for word', location='args')
Q_Parser.add_argument('page', required=False, type=int,
                        help='Number of pages', location='args')
Q_Parser.add_argument('per_page', required=False, type=int,
                        help='categories per page', default=10, location='args')

@api.route('/<int:category_id>/list')
class RecipieCollection(Resource):
    @api.response(404, 'No Recipies created by this user')
    @api.response(200, 'Recipies found')
    @api.expect(Q_Parser)
    @jwt_required
    def get(self, category_id):
        '''Returns a list of Recipies for a particular category'''

        user_id = get_jwt_identity()
        the_recz = Recipie.query.filter_by(created_by=user_id,
                                            category_id=category_id)
        args = Q_Parser.parse_args(request)
        q = args.get('q', '')
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        if q:
            the_recz = Recipie.query.filter(
                Recipie.recipie_name.like("%" + q + "%"))
                
        
        if the_recz is None:
            return {'message': 'No Recipies created by this user'}, 404
        paged_recs = the_recz.paginate(page, per_page, error_out=False)
        paginated = []
        for a_recipe in paged_recs.items:
            paginated.append(a_recipe)

        size = len(paginated)

        if size == 0:
            return {'message': 'No Recipies created by this user'}, 404
        return marshal(paginated, recipe), 200



@api.route('/<int:category_id>/create')
class RecipieCreation(Resource):
    @api.response(201, 'Recipe successfully created.')
    @api.response(409, 'Conflict, Recipie already exists')
    @api.expect(recipie_data)
    @jwt_required
    def post(self, category_id):
        ''' Creates a new Recipie attached to a particular category'''
        data = request.get_json()
        rec_name = data.get('recipie_name')
        ingredients = data.get('ingredients')
        user_id = get_jwt_identity()
        category_id = category_id
        if Recipie.query.filter_by(
                created_by=user_id,
                category_id=category_id,
                recipie_name=rec_name).first() is not None:
            return {'message': 'Conflict, Recipe already exists'}, 409
        new_rec = Recipie(recipie_name=rec_name,
                            ingredients=ingredients,
                            created_by=user_id,
                            category_id=category_id)
        new_rec.save()
        return {'Recipe id': new_rec.recipie_id,
                'message': 'Recipe successfully created.'}, 201


@api.route('/<int:category_id>/<int:recipie_id>')
@api.response(404, 'The Recipe you are querying does not exist.')
class RecipeItem(Resource):
    @api.response(200, 'Recipie Located')
    @jwt_required
    def get(self, category_id, recipie_id):
        '''Returns a recipe for a category'''
        user_id = get_jwt_identity()  
        response = Recipie.query.filter_by(
                                created_by=user_id,
                                category_id=category_id,
                                recipie_id=recipie_id
                                ).first()
        if response is None:
            return {'message': 'The Recipe you are querying does not exist'}, 404
        return marshal(response, recipe), 200

    @api.response(204, 'Recipe successfully updated.')
    @api.response(404, 'No such Recipe exists')
    @api.response(403, "Forbidden, You don't own this Recipe")
    @api.expect(recipie_data)
    @jwt_required
    def put(self, category_id, recipie_id):
        ''' Updates an categories recipie '''
        user_id = get_jwt_identity() 
        current_recipe = Recipie.query.filter_by(created_by=user_id,
                                                category_id=category_id,
                                                recipie_id=recipie_id).first()
        data = request.get_json()
        rec_name = data.get('recipie_name')
        ingrid = data.get('ingredients')
        if current_recipe is not None:
            current_recipe.recipie_name = rec_name
            current_recipe.ingredients = ingrid
            db.session.add(current_recipe)
            db.session.commit()
            return {'message': 'Recipe successfully updated.'}, 200
        return {'message': 'No such Recipe exists'}, 404


    @api.response(204, 'Recipie successfully deleted.')
    @api.response(404, 'Not Found, Recipie does not exist')
    @api.response(403, "Forbidden, You don't own this category")
    @jwt_required
    def delete(self, category_id, recipie_id):
        '''Deletes an existing Recipe'''
        user_id = get_jwt_identity() 
        current_recipe = Recipie.query.filter_by(created_by=user_id,
                                                category_id=category_id,
                                                recipie_id=recipie_id).first()
        
        if current_recipe is not None:
            db.session.delete(current_recipe)
            db.session.commit()
            return {'message': 'Recipie successfully deleted.'}, 200
        return {'message': 'Not Found, Recipie does not exist'}, 404
