from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodsView, MealsView, MealFoodsView


urlpatterns = [
    path('api/v1/foods/', FoodsView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/foods/<food_id>', FoodsView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'})),
    path('api/v1/meals/', MealsView.as_view({'get': 'list'})),
    path('api/v1/meals/<meal_id>/foods/', MealsView.as_view({'get': 'retrieve'})),
    path('api/v1/meals/<meal_id>/foods/<food_id>', MealFoodsView.as_view({'post': 'create', 'delete': 'destroy'})),
]
