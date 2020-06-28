from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurants', views.RestaurantView)
router.register('trending', views.TrendingView)
router.register('users', views.UserView)


urlpatterns = [
   path('', include(router.urls))
]