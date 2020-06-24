from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','thumb', 'name', 'cuisines', 'timings', 'url', 'address', 'phone_number', 'has_online_delivery', 'is_delivering_now', 'average_cost_for_two', 'highlights')

         
   