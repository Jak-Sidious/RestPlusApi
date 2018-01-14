from manage import app
from app import  db, app_config
from flask_testing import TestCase
class BaseTest(TestCase):

    def create_app(self):
        # self.app = create_app(config_name='testing')
        app.config.from_object(app_config['testing'])
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        # self.app = create_app(config_name='testing')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()