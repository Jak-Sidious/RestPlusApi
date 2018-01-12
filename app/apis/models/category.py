# #app/models/category.py

# from flask_bcrypt import Bcrypt
# from app import db
# from app.apis.models.user import User

# import jwt
# from datetime import datetime, timedelta

# class Category(db.Model):
#     """This class represents the category table"""

#     __tablename__ = 'categories'

#     category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     category_name = db.Column(db.String(50), nullable=False, unique=True)
#     category_description = db.Column(db.String(256), nullable=False)
#     date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
#     date_modified = db.Column(
#         db.DateTime, default=db.func.current_timestamp(),
#         onupdate=db.func.current_timestamp())
#     created_by = db.Column(db.Integer, db.ForeignKey(User.user_id))

#     def __init__(self, category_name, category_description, created_by):
#         self.category_name = category_name
#         self.category_description = category_description
#         self.created_by = created_by

#     def save(self):
#         # save a category
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         # tells python how to print objects of a class
#         return '<Categoryname: {}'.format(self.category_name)

#     # @staticmethod
#     # def getall(Category.category_id):
#     #     """Return all category elements"""
#     #     return Category.query.all()

#     def delete(self):
#         """Delete an instance of the category class"""
#         db.session.delete(self)
#         db.session.commit()
