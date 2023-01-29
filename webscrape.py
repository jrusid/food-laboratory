import requests
from bs4 import BeautifulSoup
import os

def get_api_key():
  api_key = os.getenv("yelp_api_key")
  return api_key

api_key = get_api_key()
auth_header = {"Authorization": "Bearer %s" % api_key}
api_url = "https://api.yelp.com/v3"
search_business = "/businesses/search"

def search(location, term):
  query = {
    "location": location,
    "term": term
  }
  request_url = api_url + search_business

  response = requests.get(request_url, headers=auth_header, params=query)
  return response.json()

print(search("Cambridge, MA", "cafe"))