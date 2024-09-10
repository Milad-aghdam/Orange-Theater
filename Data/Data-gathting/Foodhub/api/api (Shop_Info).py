import requests




Shop_id = 870800

### Headers SET ###
headers = {"franchise": "foodhub.co.uk", "store": f"{Shop_id}"}


### Requests ###
url = f"https://foodhub.co.uk/api/consumer/store?app_name=FRANCHISE&storeId={Shop_id}"
response = requests.get(url, headers=headers)
