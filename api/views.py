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
