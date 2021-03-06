from manage import app
from app import  db, app_config
from flask_testing import TestCase

class BaseTest(TestCase):

    def create_app(self):
        app.config.from_object(app_config['testing'])
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        self.reg_data = {
            "username": "testuser",
            "password": "testuser12345",
            "email": "test@test.com"
        }
        self.login_data = {
            "username": "testuser",
            "password": "testuser12345"
        }
        self.wrong_data ={
            "username": "testing",
            "password": "testuser12345"
        }
        self.category_data = {
            "category_name": "test category",
            "category_description" : "Test description"
        }
        self.category_data1 = {
            "category_name": "test category1",
            "category_description" : "Test description1"
        }
        self.recipe_data = {
            "recipie_name": "Test name",
            "ingredients": " Test ingredients"
        }
        self.recipe_data1 = {
            "recipie_name": "Test name1",
            "ingredients": " Test ingredients1"
        }
        self.password_reset_data = {
            "old_password": "testuser12345",
            "new_password": "testuser123"
        }
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()