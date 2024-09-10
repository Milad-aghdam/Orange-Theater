import requests
import json


######## offset ######## 
#مقدار آفست که با آن درخواست میشود، برابر است با تعداد شاپ های موجود در صفحه
#در هر نتیجه ای که این API بر میگرداند مقدار زیر وجود دارد:
### {'offset': 60, 'hasMore': True}
# این به این معنی است که تعداد کل نتایجی که برگردانده شده 60 تا هست و همچنین باز نتایجی هم برای درخواست وجود دارد
# برای درخواست نتایج بعدی باید آفست برابر با 60 شود در پیلود
# این فرایند تا زمانی ادامه میابد که hasMore برابر با False شود.








lat, lng = 50.80194782816253, -0.7742411686239181
offset = 0 









### Headers SET ###
headers = {
    'x-csrf-token': 'x',
    'Cookie': f'uev2.loc={{"latitude":{lat},"longitude":{lng}}};',
    'Content-Type': 'application/json'
}
payload = json.dumps({
    "cacheKey": "/DELIVERY///0/0//JTVCJTVE/undefined//////HOME////////",
    "feedSessionCount": {
        "announcementCount": 0,
        "announcementLabel": ""
    },
    "userQuery": "",
    "date": "",
    "startTime": 0,
    "endTime": 0,
    "carouselId": "",
    "sortAndFilters": [],
    "billboardUuid": "",
    "feedProvider": "",
    "promotionUuid": "",
    "targetingStoreTag": "",
    "venueUUID": "",
    "selectedSectionUUID": "",
    "favorites": "",
    "vertical": "",
    "searchSource": "",
    "searchType": "",
    "keyName": "",
    "serializedRequestContext": "",
    "pageInfo": {
        "offset": offset,
        "pageSize": 80
    },
    "isUserInitiatedRefresh": False
})



### Requests ###
url = "https://www.ubereats.com/_p/api/getFeedV1?localeCode=gb"
response = requests.request("POST", url, headers=headers, data=payload)


