import requests
import json
import googlemaps
import os
import pprint
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')
location = str(input("Enter city for timezone: ")) #gets user's desired city
AUTH_URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'

response = requests.get(AUTH_URL)

lat = response.json()['results'][0]['geometry']['location']['lat']
long = response.json()['results'][0]['geometry']['location']['lng']


time = int(time.time()) #get the current timestamp required for URL:

AUTH_URL2 = 'https://maps.googleapis.com/maps/'\
          f'api/timezone/json?location={lat}'\
          f'%2C{long}&timestamp={time}&key={API_KEY}'


auth_response = requests.get(AUTH_URL2)
timezone = auth_response.json()["timeZoneName"]
print(f"\nThe time zone for {location.title()} is {timezone}") 
