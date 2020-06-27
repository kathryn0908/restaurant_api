from rest_framework import serializers
from .models import Restaurant, Trending, User

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','thumb', 'name', 'cuisines', 'timings', 'url', 'address', 'phone_number', 'has_online_delivery', 'is_delivering_now', 'average_cost_for_two', 'highlights')

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trending 
        fields = ('id', 'image_url', 'url', 'title', 'description') 
          
class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'password')    
   