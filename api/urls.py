from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodsView


urlpatterns = [
    path('api/v1/foods/', FoodsView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/foods/<food_id>', FoodsView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'})),
]
