from django.contrib import admin
from .models import Restaurant, Trending, User, Review, Favorite


admin.site.register(Restaurant)
admin.site.register(Trending)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Favorite)

