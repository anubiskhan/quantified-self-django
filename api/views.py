from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializer
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
        food = Food.objects.get(id=food_id)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
