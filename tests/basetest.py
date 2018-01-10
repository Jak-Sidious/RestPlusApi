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