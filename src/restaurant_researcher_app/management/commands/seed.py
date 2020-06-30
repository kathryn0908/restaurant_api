from django.core.management.base import BaseCommand
import requests
from ...models import Restaurant, Trending

original_restaurant_url = 'https://developers.zomato.com/api/v2.1/search?count=50&lat=39.742043&lon=-104.991531&sort=rating'

class Command(BaseCommand):
  
  def handle(self, *args, **options):
    # clear_data()
    # get_trending_info()
    get_restaurant_info()
    # seed_trending()
    seed_restaurants()
    print("completed")

def get_restaurant_info():
  url = 'https://developers.zomato.com/api/v2.1/search?lat=39.742043&lon=-105.081505&radius=100'
  r = requests.get(url, headers={'Content-Type': 'application/json', "user-key": "0c1fc23671554a06d3ab8f20e69a1c95"})
  restaurant = r.json()
  return restaurant['restaurants']

  
  
  

def get_trending_info():
  url = 'https://developers.zomato.com/api/v2.1/collections?city_id=305&lat=39.742043&lon=-104.991531&count=20'
  r = requests.get(url, headers={'Content-Type': 'application/json', "user-key": "0c1fc23671554a06d3ab8f20e69a1c95"})
  trending = r.json()
  return trending['collections']
  # print(trending['collections'])
  

def seed_restaurants():
  for i in get_restaurant_info():
    restaurant= Restaurant(
      thumb=i['restaurant']['thumb'],
      name=i['restaurant']['name'],
      cuisines=i['restaurant']['cuisines'],
      timings=i['restaurant']['timings'],
      url=i['restaurant']['url'],
      address=i['restaurant']['location']['address'],
      phone_number=i['restaurant']['phone_numbers'],
      has_online_delivery=i['restaurant']['has_online_delivery'],
      is_delivering_now=i['restaurant']['is_delivering_now'],
      average_cost_for_two=i['restaurant']['average_cost_for_two'] ,
      highlights=", ".join(i['restaurant']['highlights'])
  )
    restaurant.save()
  

def seed_trending():
  for i in get_trending_info():
    trending= Trending(
      image_url=i['collection']['image_url'],
      url=i['collection']['url'],
      title=i['collection']['title'],
      description=i['collection']['description']
  )
    trending.save()


def clear_data():
  Restaurant.objects.all().delete()
  Trending.objects.all().delete()
