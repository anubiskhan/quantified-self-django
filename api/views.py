from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Food, Meal
from .serializers import FoodSerializer, MealSerializer
from django.shortcuts import get_object_or_404

class FoodsView(viewsets.ViewSet):
    def list(self, request):
        # get all foods
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def create(self, request):
        # post a new food
        name = request.data["food"]["name"]
        calories = request.data["food"]["calories"]
        food = Food.objects.create(name = name, calories = calories)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    def retrieve(self, request, food_id):
        # get a single food
        food = Food.objects.get(id=food_id)
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    def update(self, request, food_id):
        # update a single food
        name = request.data["food"]["name"]
        calories = request.data["food"]["calories"]
        food = Food.objects.get(id=food_id)
        food.name = name
        food.calories = calories
        food.save()
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)

    def destroy(self, request, food_id):
        # removes a food object
        food = Food.objects.get(id=food_id)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealsView(viewsets.ViewSet):
    def list(self, request):
        # get all meals
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, meal_id):
        # get single meal
        meal = Meal.objects.get(id=meal_id)
        serializer = MealSerializer(meal, many=False)
        return Response(serializer.data)

class MealFoodsView(viewsets.ViewSet):
    def create(self, request, meal_id, food_id):
        # add a food to a meal
        meal = Meal.objects.get(id=meal_id)
        food = Food.objects.get(id=food_id)
        meal.foods.add(food)
        message = f'Successfully added {food.name} to {meal.name}'
        return Response(message, status=status.HTTP_201_CREATED)

    def destroy(self, request, meal_id, food_id):
        # remove a food from a meal
        meal = Meal.objects.get(id=meal_id)
        food = Food.objects.get(id=food_id)
        meal.foods.remove(food)
        message = f'Successfully removed {food.name} to {meal.name}'
        return Response(message, status=status.HTTP_202_CREATED)
