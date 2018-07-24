from django.test import TestCase, Client
from api.models import Food, Meal
import json

# import pdb; pdb.set_trace()

# Create your tests here.
client = Client()

class FoodApiTest(TestCase):
    def setUp(self):
        Food.objects.create(name='Garsh', calories=101)
        Food.objects.create(name='Darsh', calories=123)

    def test_food_list_endpoint(self):
        response = client.get('/api/v1/foods/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], 'Garsh')
        self.assertEqual(json.loads(response.content)[0]['calories'], 101)
        self.assertEqual(json.loads(response.content)[1]['name'], 'Darsh')
        self.assertEqual(json.loads(response.content)[1]['calories'], 123)

class MealApiTest(TestCase):
    def setUp(self):
        Meal.objects.create(name='Breakfast')
        Meal.objects.create(name='Snack')

    def test_meal_list_endpoint(self):
        response = client.get('/api/v1/meals/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], 'Breakfast')
        self.assertEqual(json.loads(response.content)[1]['name'], 'Snack')
