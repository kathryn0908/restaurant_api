from django.core.management.base import BaseCommand
import requests
from ...models import Restaurant

class Command(BaseCommand):
  
  def handle(self, *args, **options):
    get_restaurant_info()
    seed_restaurants()
    clear_data()
    print("completed")

def get_restaurant_info():
  url = 'https://developers.zomato.com/api/v2.1/search?count=1&lat=39.742043&lon=-104.991531&radius=20mi'
  r = requests.get(url, headers={'Content-Type': 'application/json', "user-key": "0c1fc23671554a06d3ab8f20e69a1c95"})
  restaurant = r.json()
  return restaurant

def seed_restaurants():
  for i in get_restaurant_info():
    restaurant= Restaurant(
      thumb=i['restaurants'][0]['restaurant']['thumb'],
      name=i['restaurants'][0]['restaurant']['name'],
      cuisines=i['restaurants'][0]['restaurant']['cuisines'],
      timings=i['restaurants'][0]['restaurant']['timings'],
      url=i['restaurants'][0]['restaurant']['url'],
      address=i['restaurants'][0]['restaurant']['location']['address']+','+restaurant['restaurants'][0]['restaurant']['location']['city'],
      phone_number=i['restaurants'][0]['restaurant']['phone_numbers'],
      has_online_delivery=i['restaurants'][0]['restaurant']['has_online_delivery'],
      is_delivering_now=i['restaurants'][0]['restaurant']['is_delivering_now'],
      average_cost_for_two=i['restaurants'][0]['restaurant']['average_cost_for_two'] ,
      highlights=i['restaurants'][0]['restaurant']['highlights']
  )
  restaurant.save()
  print('it works')

def clear_data():
  Restaurant.objects.all().delete()
