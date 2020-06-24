from django.core.management.base import BaseCommand
import requests
from ...models import Restaurant


def get_restaurant_info():
  url = 'https://developers.zomato.com/api/v2.1/search?count=50&lat=39.742043&lon=-104.991531&sort=real_distance'
  r = requests.get(url, headers={'Content-Type': 'application/json'})
  restaurant = r.json()
  return restaurant


print(get_restaurant_info)