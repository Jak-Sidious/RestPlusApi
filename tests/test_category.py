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
        self.assertEqual(catres.status_code, 201)
        catres2 = json.loads(catres.data)
        self.assertEqual(catres2 ['message'], 'Category successfully created')


    def test_category_cant_be_created_twice(self):
        '''Test that categories can be listed'''
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        token = json.loads(res1.data)['token']
        catres = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        catres1 = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        msg = json.loads(catres1.data)
        self.assertEqual(catres1.status_code, 409)
        self.assertEqual(msg['message'], 'Category already exists')

    def test_can_edit_category(self):
        '''Test that category can be edited'''
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        token = json.loads(res1.data)['token']
        catres = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        catres1 = self.client.put("/apiv1/category/1",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data1))
        msg = json.loads(catres1.data)
        self.assertEqual(catres1.status_code, 200)
        self.assertEqual(msg['message'], 'Category successfully updated')

    def test_can_view_category(self):
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        token = json.loads(res1.data)['token']
        catres = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        catview = self.client.get("/apiv1/category/1",
                                headers = {'Authorization': 'Bearer '+ token}, 
                                content_type="application/json",
                                data=json.dumps(self.category_data1))
        # print (catview)
        msg = json.loads(catview.data)
        # print (msg['message'])
        self.assertEqual(catres.status_code, 201)

    def test_can_delete_category(self):
        res = self.app.post("/apiv1/users/register", data=json.dumps(self.reg_data), content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", data=json.dumps(self.login_data), content_type="application/json")
        token = json.loads(res1.data)['token']
        catres = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        catdelete = self.client.delete("/apiv1/category/1",
                                headers = {'Authorization': 'Bearer '+ token}, 
                                content_type="application/json",
                                data=json.dumps(self.category_data1))
        # msg = json.loads(catdelete.data)
        # print (msg['message'])
        self.assertEqual(catdelete.status_code, 204)
