import requests
#import json

### Headers SET ###
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}




### Requests ###
lat, lng = 50.80194782816253, -0.7742411686239181

url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched?latitude={lat}&longitude={lng}"
response = requests.get(url, headers=headers)


#print(json.dumps(response.json(), indent=4))