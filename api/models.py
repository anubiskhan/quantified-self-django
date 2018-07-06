from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meal(models.Model):
    name = models.CharField(max_length=200)
    foods = models.ManyToManyField(Food)
