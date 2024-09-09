import requests


### Headers SET ###
id = 870800

url = f"https://foodhub.co.uk/api/consumer/store?app_name=FRANCHISE&storeId={id}"
headers = {"franchise": "foodhub.co.uk", "store": f"{id}"}


### Requests ###
response = requests.get(url, headers=headers)