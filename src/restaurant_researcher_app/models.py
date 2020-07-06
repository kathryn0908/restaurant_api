from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
import datetime




# Create your models here.
class Restaurant(models.Model):
    thumb = models.TextField()
    name = models.CharField(max_length=50)
    cuisines = models.CharField(max_length=50)
    timings = models.TextField()
    url = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    has_online_delivery = models.TextField()
    is_delivering_now = models.TextField()
    average_cost_for_two = models.PositiveIntegerField()
    highlights = JSONField()
    

class Trending(models.Model):
    image_url= models.TextField()
    url= models.TextField()
    title= models.TextField()
    description= models.TextField()

class User(AbstractUser):
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Favorite(models.Model):
    user = models.ForeignKey(
        User, 
        related_name="favorites", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="favorites",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Review(models.Model):
    review = models.TextField(null=True)
    name = models.TextField(null=True)
    user = models.ForeignKey(
        User, 
        related_name="reviews", 
        on_delete=models.CASCADE,
        null=True 
    )
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="reviews",
        on_delete=models.CASCADE,
        null=True
    )
    
    rating = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class StarRating(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(
        User, 
        related_name="ratings", 
        on_delete=models.CASCADE,
        null=True 
    )
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="ratings",
        on_delete=models.CASCADE,
        null=True
    )
   
    


    
    

    


    

