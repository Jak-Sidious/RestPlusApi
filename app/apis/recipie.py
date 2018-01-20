from flask import request
from flask_restplus import Resource, Namespace, fields, marshal
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

category_list = api.model('category', {
    'user_id': fields.Integer(readOnly=True, description='User that made the category'),
    'category_id': fields.Integer(readOnly=True, description='Unique identifier for each category'),
    'category_name': fields.String(required=True, description='category name'),
    'category_description': fields.String(required=True, description='A description about the current category'),
    'date_created': fields.DateTime(readOnly=True, description='Date created'),
    'date_modified': fields.DateTime(readOnnly=True, description='date modified'),
    'recipies': fields.String(readOnly=True, description='Recipies belonging to a certain category')

})


@api.route('/<int:category_id>/list')
class RecipieCollection(Resource):
    @api.response(404, 'No Recipies created by this user')
    @api.response(200, 'Recipies found')
    @jwt_required
    def get(self, category_id):
        """Returns a list of Recipies for a particular category"""

        user_id = get_jwt_identity()
        the_recz = Recipie.query.filter_by(created_by=user_id,
                                            category_id=category_id)
        if the_recz is None:
            return {'message': 'No Recipies created by this user'}, 404
        paged_recs = the_recz.paginate(error_out=False)
        paginated = []
        for a_recipe in paged_recs.items:
            paginated.append(a_recipe)


        return marshal(paginated, recipe), 200



@api.route('/<int:category_id>/create')
class RecipieCreation(Resource):
    @api.response(201, 'Recipe successfully created.')
    @api.response(409, 'Conflict, Recipie already exists')
    @api.expect(recipie_data)
    @jwt_required
    def post(self, category_id):
        """ Creates a new Recipie attached to a particular category"""
        data = request.get_json()
        rec_name = data.get('recipie_name')
        ingedients = data.get('ingedients')
        user_id = get_jwt_identity()
        category_id = category_id
        if Recipie.query.filter_by(
                created_by=user_id,
                category_id=category_id,
                recipie_name=rec_name).first() is not None:
            return {'message': 'Conflict, Recipe already exists'}, 409
        new_rec = Recipie(recipie_name=rec_name,
                            ingredients=ingedients,
                            created_by=user_id,
                            category_id=category_id)
        new_rec.save()
        return {'message': 'Recipe successfully created.'}, 201


# modify to cater to the redesigned routes
@api.route('/<int:category_id>/<int:recipie_id>')
@api.response(404, 'The Recipe you are querying does not exist.')
class RecipeItem(Resource):
    @api.response(200, 'Recipie Located')
    @jwt_required
    def get(self, category_id, recipie_id):
        """Returns a recipe for a categ0ry"""
        user_id = get_jwt_identity()
        response = Recipie.query.filter_by(created_by=user_id,
                                            category_id=category_id).first()
        if response is None:
            return {'message': 'The Recipe you are querying does not exist'}, 404
        return marshal(response, recipe), 200
        pass

    @api.response(204, 'Recipe successfully updated.')
    @api.response(404, 'No such Recipe exists')
    @api.response(403, "Forbidden, You don't own this Recipe")
    @api.expect(recipie_data)
    def put(self, category_id, recipie_id):
        """ Updates an categories recipie """
        pass


    @api.response(204, 'Recipie successfully deleted.')
    @api.response(404, 'Not Found, Recipie does not exixt')
    @api.response(403, "Forbidden, You don't own this category")
    def delete(self, category_id, recipie_id):
        """Deletes an existing Recipe"""
        pass
