import json

from tests import BaseTest
from app.models.user import User
class UserTest(BaseTest):
    '''Tests for the user category'''

    def test_registration_succesful(self):
        '''Ensure a user can be added to the database'''
        
        response = self.app.post("/apiv1/users/register", 
                                data=json.dumps(self.reg_data), 
                                content_type="application/json")
        msg = json.loads(response.data)

        self.assertIn(msg['message'], 'User succesfully registered')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.query.count(), 1)

    def test_login_succesful(self):
        '''Ensure a user can login successfully'''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        msg = json.loads(res1.data)
        self.assertIn(msg['response'], 'User sucessfully Loged in')
        self.assertEqual(res1.status_code, 200)
    
    def test_unregistered_user_login_fails(self):
        ''' Test if an unregistered user can sign in '''
        res = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        msg = json.loads(res.data)
        self.assertIn(msg['message'], 'The requested username is unavailable')
        self.assertEqual(res.status_code, 404)

    def test_user_cant_register_twice(self):
        '''Test that a user cannot register twice '''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        msg = json.loads(res1.data)
        self.assertIn(msg['message'], 'Username testuser already exists')
        self.assertEqual(res1.status_code, 409)

    def test_user_can_logout(self):
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        logout_res = self.app.delete("apiv1/users/logout", 
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json")
        msg = json.loads(logout_res.data)
        self.assertIn(msg['message'], 'You have been logged out')
        self.assertEqual(logout_res.status_code, 200)

    def test_user_can_rest_password(self):
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        reset_res = self.app.put("/apiv1/users/resetpassword",
                                headers = {'Authorization': 'Bearer '+ token},
                                data=json.dumps(self.password_reset_data),
                                content_type="application/json")
        msg = json.loads(reset_res.data)
        self.assertIn(msg['message'], 'Password reset successfully')
        self.assertEqual(reset_res.status_code, 200)

    