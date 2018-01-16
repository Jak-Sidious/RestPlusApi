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
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()