from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

@api_view(['GET'])
def get_foods(request):
    # get all foods
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def post_food(request):
    # post a new food
    name = request.data["food"]["name"]
    calories = request.data["food"]["calories"]
    food = Food.objects.create(name = name, calories = calories)
    serializer = FoodSerializer(food, many=False)
    return Response(serializer.data)
