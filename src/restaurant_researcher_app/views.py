from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant, Trending, User
from .serializers import RestaurantSerializer, TrendingSerializer, UserSerializer



class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class TrendingView(viewsets.ModelViewSet):
    queryset = Trending.objects.all()
    serializer_class = TrendingSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Create your views here.
