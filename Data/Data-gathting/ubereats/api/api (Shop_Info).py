import requests
import json 


### Headers SET ###
headers = {
    'x-csrf-token': 'x',
}




### Requests ###
url = 'https://www.ubereats.com/_p/api/getStoreV1?localeCode=gb'

storeUuid ="35c45860-9733-4510-afb6-ef3df54a5639"
payload = {
    "storeUuid": storeUuid,
    "diningMode": "DELIVERY",
    "time": {"asap":True},
    "cbType": "EATER_ENDORSED"
}
response = requests.post(url, headers=headers, json=payload)






#print(f"Status Code: {response}")
#print("Response JSON:", json.dumps(response.json(), indent=4))
