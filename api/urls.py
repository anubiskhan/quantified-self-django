from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/foods/', views.get_foods, name='get_foods'),
    path('api/v1/foods', views.post_food, name='post_food'),
]
