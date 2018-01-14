import json

from tests import BaseTest

class CategoryTest(BaseTest):
    """Test for the Category functionality"""

    def test_category_succesfully_created(self):
        user_data = {
            "username": "testuser",
            "password": "testuser12345"
        }

        category_data = {
            'category_name' : 'Test category',
            'category_description' : 'Test category Description'
        }
        response = self.app.post("/apiv1/category/create", data=json.dumps(category_data), content_type="application/json")
        msg = json.loads(response.data)

        self.assertIn(msg['message'], 'Category successfully created.')
        self.assertEqual(response.status_code, 201)

