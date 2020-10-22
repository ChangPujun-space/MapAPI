!pip install routingpy
from routingpy import ORS
apis = (
   (ORS(api_key='5b3ce3597851110001cf6248bfc912cf0bab4d3c943e5d29b91ad19d'), 'driving-car')
)
coords = [[136.676102,36.554878], [136.620859,36.450928]]
client, profile = apis
route = client.directions(locations=coords, profile=profile)
print("Direction - {}:\n\tDuration: {}\n\tDistance: {}".format(client.__class__.__name__,
                                                                   route.duration,
                                                                   route.distance))