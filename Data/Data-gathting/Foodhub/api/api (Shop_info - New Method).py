import requests




Shop_id = 873615
Host = "bayroot.co.uk"
### Headers SET ###
headers = {"franchise": "foodhub.co.uk", "store": f"{Shop_id}"}


### Requests ###
url = f"{Host}/api/consumer/store?app_name=FRANCHISE&storeId={Shop_id}"
response = requests.get(url, headers=headers)
