from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('id','thumb', 'name', 'cuisines', 'timings', 'url', 'address', 'phone_number', 'has_online_delivery', 'is_delivering_now', 'average_cost_for_two', 'highlights')

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trending 
        fields = ('id', 'image_url', 'url', 'title', 'description') 
          
class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.User
            fields = ('id', 'username', 'email', 'password') 
            # extra_kwargs = {'password': {'write-only': True}, 'username': {'read_only': True}, 'email': {'read_only': True}}
            
        def create(self, validated_data):
            user = models.User(
                email = validated_data['email'],
                username = validated_data['username'],
                password = make_password(validated_data['password'])
            )
        
            user.save()

            return user   
   