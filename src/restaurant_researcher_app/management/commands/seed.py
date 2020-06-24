from django.core.management.base import BaseCommand
import requests
from ...models import Restaurant

class Command(BaseCommand):
  
  def handle(self, *args, **options):
    get_restaurant_info()
    seed_restaurants()
    print("completed")

def get_restaurant_info():
  url = 'https://developers.zomato.com/api/v2.1/search?count=1&lat=39.742043&lon=-104.991531&radius=20mi'
  r = requests.get(url, headers={'Content-Type': 'application/json', "user-key": "0c1fc23671554a06d3ab8f20e69a1c95"})
  restaurant = r.json()
  return restaurant['restaurants']

def seed_restaurants():
  for i in get_restaurant_info():
    restaurant= Restaurant(
      thumb=i['restaurant']['thumb'],
      name=i['restaurant']['name'],
      cuisines=i['restaurant']['cuisines'],
      timings=i['restaurant']['timings'],
      url=i['restaurant']['url'],
      address=i['restaurant']['location']['address']+','+i['restaurant']['location']['city'],
      phone_number=i['restaurant']['phone_numbers'],
      has_online_delivery=i['restaurant']['has_online_delivery'],
      is_delivering_now=i['restaurant']['is_delivering_now'],
      average_cost_for_two=i['restaurant']['average_cost_for_two'] ,
      highlights=i['restaurant']['highlights']
  )
  restaurant.save()
  print('it works')

def clear_data():
  Restaurant.objects.all().delete()
