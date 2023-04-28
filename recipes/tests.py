from django.test import TestCase
from rest_framework.test import APIClient

class RecipeTestCase(TestCase):
    def test_recipe_list(self):
        client = APIClient()
        response = client.get('/recipes/')
        self.assertEquals(response.status_code, 200)
