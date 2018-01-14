import json

from tests import BaseTest
from app.models.user import User
from app.models.category import Category


class CategoryTest(BaseTest):
    """Test for the Category functionality"""

    def test_category_succesfully_created(self):
        
        cat_test_user = User('testuser', 'testpass')
        cat_test_user.save()
        category_data = {
            'category_name' : 'Test category',
            'category_description' : 'Test category Description',
            'user_id': cat_test_user.user_id
        }
        response = self.app.post("/apiv1/category/create", data=json.dumps(category_data), content_type="application/json")
        msg = json.loads(response.data)

        self.assertIn(msg['message'], 'Category successfully created.')
        self.assertEqual(response.status_code, 201)

    def test_list_categories(self):
        cat_test_user = User('testuser', 'testpass')
        cat_test_user.save()
        category_data1 = {
            'category_name' : 'Test category1',
            'category_description' : 'Test category Description',
            'user_id': cat_test_user.user_id
        }
        self.app.post("/apiv1/category/create", data=json.dumps(category_data1), content_type="application/json")
        category_data2 = {
            'category_name' : 'Test category2',
            'category_description' : 'Test category Description2',
            'user_id': cat_test_user.user_id
        }
        self.app.post("/apiv1/category/create", data=json.dumps(category_data2), content_type="application/json")

        response = self.app.get("/apiv1/category/list")

        

