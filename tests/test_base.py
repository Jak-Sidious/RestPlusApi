# app/tests/basetest.py
# from flask_testing import TestCase
# from app.instance.config import app_config

# from run import app

# class BaseTest(TestCase):

#     def create_app(self):
#         app.config.from_object(app_config['testing'])
#         app.config.from_pyfile('config.py')
#         return app

#     def setUp(self):
#         self.app = self.create_app().test_client()

#     def tearDown(self):
#         pass

from flask_testing import TestCase
from instance.config import app_config
# /Users/jakanakiwanuka/work/RestplusDemo/app/instance/config.py

# from run import app
#from app import db
# from app import create_app, db

# class BaseTest(TestCase):

#     def create_app(self):
#         app.config.from_object(app_config['testing'])
#         db.init_app(app)
#         return app

#     def setUp(self):
#         self.app = self.create_app().test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()