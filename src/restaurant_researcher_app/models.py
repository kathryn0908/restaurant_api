from jsonfield import JSONField
from django.db import models



# Create your models here.
class Restaurant(models.Model):
    thumb = models.TextField()
    name = models.CharField(max_length=50)
    cuisines = models.CharField(max_length=50)
    timings = models.TextField()
    url = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    has_online_delivery = models.BooleanField()
    is_delivering_now = models.BooleanField()
    average_cost_for_two = models.PositiveIntegerField()
    highlights = JSONField()

class Trending(models.Model):
    image_url= models.TextField()
    url= models.TextField()
    title= models.TextField()
    description= models.TextField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
   
    

