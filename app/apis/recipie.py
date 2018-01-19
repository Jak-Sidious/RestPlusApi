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
    'ingedients': fields.String(required=True, description='A description of the ingredients to compile the recipie'),
    'created_by': fields.Integer(readOnly=True, description='Which User created this nanka'),
    'category_id': fields.Integer(readOnly=True, description='Which category does this recipe belong to'),
    'date_created': fields.DateTime(readOnly=True, description='Date Created'),
    'date_modified': fields.DateTime(readOnly=True, description='Date modified')
})


recipie_data = api.model('create recipie', {
    'recipie_name': fields.String(required=True, description='Name of the current recipe'),
    'ingedients': fields.String(required=True, description='The ingredients for this recipie')
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

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
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

        return marshal(the_recz, recipe), 200


@api.route('/<int:category_id>/create')
class RecipieCreation(Resource):
    @api.response(201, 'Category successfully created.')
    @api.response(409, 'Conflict, Category already exists')
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
                category_id=category_id).first() is not None:
            return {'message': 'Conflict, Category already exists'}, 409
        new_rec = Recipie(recipie_name=rec_name,
                            ingredients=ingedients,
                            created_by=user_id,
                            category_id=category_id)
        new_rec.save()
        return {'message': 'Category successfully created.'}, 201

# modify to cater to the redesigned routes
@api.route('/<int:category_id>/<int:recipie_id>')
@api.response(404, 'The Recipe you are querying does not exist.')
class RecipeItem(Resource):
    @api.response(200, 'Recipie Located')
    @jwt_required
    def get(self, category_id, recipie_id):
        """Returns a recipe for a categpry"""
        # user_id = get_jwt_identity()
        # response = Recipie.query.filter_by(created_by=user_id,
        #                                     category_id=category_id).first()
        # if response is None:
        #     return {'message': 'The Recipe you are querying foes not exist'}, 404
        # return marshal(response, recipe), 200
        pass

    @api.response(204, 'Recipe successfully updated.')
    @api.response(404, 'No such Recipe exists')
    @api.response(403, "Forbidden, You don't own this Recipe")
    @api.expect(recipie_data)
    def put(self, category_id, recipie_id):
        """ Updates an categories recipie """
        # user_id = get_jwt_identity()
        # edit_rec = Recipie.query.filter_by(created_by=user_id,
        #                                     category_id=category_id).first()
        # if edit_rec is None:
        #     return {'message': 'No such Recipe exists'}, 404
        # data = request.get_json()
        # edit_rec.recipie_name = data.get('recipie_name')
        # edit_rec.ingedients = data.get('ingedients')
        # db.session.add(edit_rec)
        # db.session.commit()
        # return {'message': 'Recipe successfully updated.'}, 204
        pass

    @api.response(204, 'Recipie successfully deleted.')
    @api.response(404, 'Not Found, Recipie does not exixt')
    @api.response(403, "Forbidden, You don't own this category")
    def delete(self, category_id, recipie_id):
        """Deletes an existing Recipe"""
        # user_id = get_jwt_identity()
        # the_rec = Recipie.query.filter_by(created_by=user_id,
        #                                     category_id=category_id).first()

        # if the_rec is not None:
        #     db.session.delete(the_rec)
        #     db.session.commit()
        #     return {'message': 'Recipie successfully deleted.'}, 204
        # return {'message': 'Not Found, Recipie does not exixt'}, 404
        pass
