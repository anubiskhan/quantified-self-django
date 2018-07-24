from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Food, Meal
from .serializers import FoodSerializer, MealSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

class FoodsView(viewsets.ViewSet):
    def list(self, request):
        # get all foods
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def create(self, request):
        # post a new food
        if "name" and "calories" in request.data["food"]:
            name = request.data["food"]["name"]
            calories = request.data["food"]["calories"]
            food = Food.objects.create(name = name, calories = calories)
            serializer = FoodSerializer(food, many=False)
            return Response(serializer.data)
        else:
            return HttpResponse(status=400)

    def retrieve(self, request, food_id):
        # get a single food
        food = get_object_or_404(Food, id=food_id)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    def update(self, request, food_id):
        # update a single food
        food = get_object_or_404(Food, id=food_id)
        if "name" and "calories" in request.data["food"]:
            food.name = request.data["food"]["name"]
            food.calories = request.data["food"]["calories"]
            food.save()
            serializer = FoodSerializer(food, many=False)
            return Response(serializer.data)
        else:
            return HttpResponse(status=400)

    def destroy(self, request, food_id):
        # removes a food object
        food = get_object_or_404(Food, id=food_id)
        food.delete()
        return HttpResponse(status=204)

class MealsView(viewsets.ViewSet):
    def list(self, request):
        # get all meals
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, meal_id):
        # get single meal
        meal = get_object_or_404(Meal, id=meal_id)
        serializer = MealSerializer(meal, many=False)
        return Response(serializer.data)

class MealFoodsView(viewsets.ViewSet):
    def create(self, request, meal_id, food_id):
        # add a food to a meal
        meal = get_object_or_404(Meal, id=meal_id)
        food = get_object_or_404(Food, id=food_id)
        meal.foods.add(food)
        message = f'Successfully added {food.name} to {meal.name}'
        return HttpResponse(json.dumps(message), status=201)

    def destroy(self, request, meal_id, food_id):
        # remove a food from a meal
        meal = get_object_or_404(Meal, id=meal_id)
        food = get_object_or_404(Food, id=food_id)
        meal.foods.remove(food)
        message = f'Successfully removed {food.name} from {meal.name}'
        return HttpResponse(json.dumps(message), status=202)
