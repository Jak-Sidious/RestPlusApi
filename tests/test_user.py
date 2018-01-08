import unittest
import json
from app import create_app, db
# /Users/jakanakiwanuka/work/RestplusDemo/app/app/__init__.py
# /Users/jakanakiwanuka/work/RestplusDemo/app/app/__init__.py
# /Users/jakanakiwanuka/work/RestplusDemo/app/tests/test_user.py

class AuthTestCase(unittest.TestCase):
    """Test case for authentication blueprint."""

    def setUp(self):
       """Set up test variables."""
       self.app = create_app(config_name="testing")
       # initialize the test client
       self.client = self.app.test_client
       # This is the user test json data with ap redefined email and password
       self.user_data = {
           'username': 'tester',
           'password': 'test_password'
       }

       with self.app.app_context():
           db.session.close()
           db.drop_all()
           db.create_all()

    def test_registration(self):
        """Test user registration work correctly."""
        print(self.user_data, '.............>>>')
        res = self.client().post(
            '/auth/register', data=json.dumps(self.user_data),
            content_type='application/json'
        )
        print (res.data.decode(), '******************')
        #  get the results returned in jso nformat
        results = json.loads(res.data.decode())
        # assert that the request contains a success message and a s201 status code
        self.assertEqual(results['message'], "You registered succesfully. Please log in.")
        self.assertEqual(res.status_code, 201)

    def test_already_registered_user(self):
        """Test that a user cannot be registered twice"""
        res = self.client().post(
            '/auth/register', data=json.dumps(self.user_data), content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)
        second_res = self.client().post(
            '/auth/register', data=json.dumps(self.user_data), content_type='application/json'
        )
        self.assertEqual(second_res.status_code, 202)
        # get the results returned in json format
        result = json.loads(second_res.data.decode())
        self.assertEqual(
            result['message'], "User already exists. Please login"
        )

    def tearDown(self):
        """Handle the deletion of data at the end of the testing"""
        with self.app.app_context():

            db.session.close()
            db.drop_all()