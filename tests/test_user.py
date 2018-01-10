import json

from . import BaseTest

class UserTest(BaseTest):
    """Ensure a user can be added to the database"""

    def test_registration_succesful(self):
        user_data = {
            "username": "testuser",
            "password": "testuser12345"
        }
        response = self.app.post("/users/register", data=json.dumps(user_data), content_type="application/json")
        msg = json.loads(response.data)
        print (msg)

        self.assertIn(msg['message'], 'User succesfully registered')
        self.assertEqual(response.status_code, 201)