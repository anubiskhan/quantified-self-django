from django.shortcuts import render
from django.http import JsonResponse
from ./models.py import Food
import json

# Create your views here.
def food_index(request):
    return JsonResponse(Food.objects.all())
