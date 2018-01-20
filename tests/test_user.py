import json

from tests import BaseTest
from app.models.user import User
class UserTest(BaseTest):
    """Tests for the user category"""

    
    # pass and fail tests
    def test_registration_succesful(self):
        """Ensure a user can be added to the database"""
        
        response = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        msg = json.loads(response.data)

        self.assertIn(msg['message'], 'User succesfully registered')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.query.count(), 1)

    def test_login_succesful(self):
        """Ensure a user can login successfully"""
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        msg = json.loads(res1.data)
        self.assertIn(msg['response'], 'User sucessfully Loged in')
        self.assertEqual(res1.status_code, 200)
    
    def test_unregistered_user_login_fails(self):
        ''' Test if an unregistered user can sign in '''
        res = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        msg = json.loads(res.data)
        self.assertIn(msg['message'], 'User not registered')
        self.assertEqual(res.status_code, 404)
        
