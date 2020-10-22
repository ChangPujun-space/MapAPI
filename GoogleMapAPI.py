!pip3 install -U googlemaps
from datetime import datetime
import time

!pip install responses
import responses

import googlemaps
API_key = 'A****************************'#enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)

distance_list=[]

Map_list=[[35.725757,139.797454],[35.717476,139.803814],[35.717967,139.790271]]
for i in Map_list:
  for j in Map_list[Map_list.index(i)+1:Map_list.index(i)+2]:
    result = gmaps.distance_matrix(tuple(i), tuple(j), mode='walking')
    distance_list.append(result["rows"][0]["elements"][0]["distance"]["value"])
print(distance_list)