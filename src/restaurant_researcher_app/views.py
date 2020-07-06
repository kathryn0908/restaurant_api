from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Restaurant, Trending, User, Review, Favorite, StarRating
from .serializers import RestaurantSerializer, TrendingSerializer, UserSerializer, ReviewSerializer, FavoriteSerializer, StarRatingSerializer



class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.AllowAny,)
    

    def __str__(self):
        return self.restaurant_text

class TrendingView(viewsets.ModelViewSet):
    queryset = Trending.objects.all()
    serializer_class = TrendingSerializer
    permission_classes = (permissions.AllowAny,)
    

    def __str__(self):
        return self.trending_text

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.AllowAny,)

class FavoriteView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.AllowAny,)

class StarRatingView(viewsets.ModelViewSet):
    queryset = StarRating.objects.all()
    serializer_class = StarRatingSerializer
    permission_classes = (permissions.AllowAny,)

