from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/foods/$',
        views.get_foods,
        name='get_foods'
    )
]
