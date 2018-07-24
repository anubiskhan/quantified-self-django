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

    def test_single_food_endpoint_success(self):
        response = client.get('/api/v1/foods/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Garsh')

    def test_single_food_endpoint_failure(self):
        response = client.get('/api/v1/foods/3')
        self.assertEqual(response.status_code, 404)

    def test_post_food_endpoint_success(self):
        response = client.post('/api/v1/foods/', '{ "food": { "name": "Blorsh", "calories": "66"} }', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Blorsh')
        self.assertEqual(json.loads(response.content)['calories'], 66)

    def test_post_food_endpoint_failure(self):
        response = client.post('/api/v1/foods/', '{ "food": { "name": "Blorsh"} }', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_patch_food_endpoint_success(self):
        response = client.patch('/api/v1/foods/1', '{ "food": { "name": "Blorsh", "calories": "66"} }', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Blorsh')
        self.assertEqual(json.loads(response.content)['calories'], 66)

    def test_patch_food_endpoint_failure(self):
        response = client.patch('/api/v1/foods/1', '{ "food": { "name": "Blorsh"} }', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_food_endpoint_success(self):
        response = client.delete('/api/v1/foods/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_food_endpoint_failure(self):
        response = client.delete('/api/v1/foods/111')
        self.assertEqual(response.status_code, 404)


class MealApiTest(TestCase):
    def setUp(self):
        Meal.objects.create(name='Breakfast')
        Meal.objects.create(name='Snack')

    def test_meal_list_endpoint(self):
        response = client.get('/api/v1/meals/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], 'Breakfast')
        self.assertEqual(json.loads(response.content)[1]['name'], 'Snack')
