from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class RestaurantSerializer(serializers.ModelSerializer):
    reviews = serializers.CharField(required=False)
    favorites = serializers.CharField(required=False)
    class Meta:
        model = models.Restaurant
        fields = ('id','thumb', 'name', 'cuisines', 'timings', 'url', 'address', 'phone_number', 'has_online_delivery', 'is_delivering_now', 'average_cost_for_two', 'highlights', 'favorites', 'reviews')

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trending 
        fields = ('id', 'image_url', 'url', 'title', 'description') 
          
class UserSerializer(serializers.ModelSerializer):
        reviews = serializers.CharField(required=False)
        favorites = serializers.CharField(required=False)
        class Meta:
            model = models.User
            fields = ('id', 'username', 'email', 'password', 'favorites', 'reviews') 
            
            
        def create(self, validated_data):
            user = models.User(
                email = validated_data['email'],
                username = validated_data['username'],
                password = make_password(validated_data['password'])
            )
        
            user.save()

            return user   

class FavoriteSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Favorite 
            fields = ('__all__') 

class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Review
            fields = ()


   