import json

from tests import BaseTest
from app.models.user import User
from app.models.category import Category


class CategoryTest(BaseTest):
    """Test for the Category functionality"""

    def test_category_succesfully_created(self):
        
        '''Test that a catgory can be created'''
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        token = json.loads(res1.data)['token']
        
        catres = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        self.assertEqual(catres .status_code, 201)
        catres2 = json.loads(catres.data)
        self.assertEqual(catres2 ['message'], 'Category successfully created')