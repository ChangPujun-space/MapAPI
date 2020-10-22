import requests
import json

payload = {
    "origins": [{"latitude": 47.6044, "longitude": -122.3345}],
    "destinations": [{"latitude": 45.5347, "longitude": -122.6231}],
    "travelMode": "driving",
}

paramtr = {"key": "AkTE-PlTPGF1iWe58hXKln6yI5wse3iBX2jIIZxsUqHrvPSjSHNXJe9ljLInwugP"}

r = requests.post('https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix', data = 
json.dumps(payload), params = paramtr)

print(r.json())
