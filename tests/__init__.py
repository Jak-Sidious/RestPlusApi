from flask_testing import TestCase
from instance.config import app_config
# /Users/jakanakiwanuka/work/RestplusDemo/app/instance/config.py

from run import app
from app import db

class BaseTest(TestCase):

    def create_app(self):
        app.config.from_object(app_config['testing'])
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()