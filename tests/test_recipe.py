import json

from tests import BaseTest
from app.models.user import User
from app.models.category import Category
from app.models.recipie import Recipie

class RecipeTest(BaseTest):
    '''Test for the Category functionality'''

    def test_recipe_can_be_succesfully_created(self):
        
        '''Test that a recipie can be created'''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        rec_create = json.loads(cat.data)
                                    
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        rec_create = json.loads(rec.data)
        self.assertEqual(rec.status_code, 201)
        self.assertEqual(rec_create['message'], 'Recipe successfully created.')


    def test_recipie_cant_be_created_twice(self):
        '''Test that duplicate recipies can't be created'''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
                                    
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        rec2 = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        msg = json.loads(rec2.data)
        self.assertEqual(rec2.status_code, 409)
        self.assertEqual(msg['message'], 'Conflict, Recipe already exists')

    def test_recipes_can_be_listed(self):
        '''Test that more than one recipie can be listed'''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        rec2 = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data1))
        listres = self.client.get("apiv1/recipes/1/list",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json")
        self.assertEqual(listres.status_code, 200)
        
    def test_recipe_can_be_viewed(self):
        '''Test that a recipie can be viewed'''
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        view_res = self.client.get("/apiv1/recipes/1/1",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json")
        self.assertEqual(view_res.status_code, 200)

    def test_recipe_can_be_edited(self):
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        edit_rec = self.client.put("/apiv1/recipes/1/1",
                                    headers = {'Authorization': 'Bearer '+ token},
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data1))
        msg = json.loads(edit_rec.data)
        self.assertEqual(edit_rec.status_code, 200)
        self.assertIn(msg['message'], 'Recipe successfully updated.')

    def test_recipe_can_be_deleted(self):
        res = self.app.post("/apiv1/users/register", 
                            data=json.dumps(self.reg_data), 
                            content_type="application/json")
        res1 = self.app.post("/apiv1/users/login", 
                            data=json.dumps(self.login_data), 
                            content_type="application/json")
        token = json.loads(res1.data)['token']
        
        cat = self.client.post("/apiv1/category/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.category_data))
        rec = self.client.post("/apiv1/recipes/1/create",
                                    headers = {'Authorization': 'Bearer '+ token}, 
                                    content_type="application/json",
                                    data=json.dumps(self.recipe_data))
        delete_rec = self.client.delete("/apiv1/recipes/1/1",
                                        headers = {'Authorization': 'Bearer '+ token}, 
                                        content_type="application/json",
                                        data=json.dumps(self.recipe_data))
        msg = json.loads(delete_rec.data)
        self.assertEqual(delete_rec.status_code, 200)
        self.assertIn(msg['message'], 'Recipie successfully deleted.')

