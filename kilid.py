import requests
import time

data = {"locations": [{"type": "city", "locationId": "2301021576"}], "subType": "sale", "type": "listing",
        "sort": "kilid,DESC", "numBedJoinComma": "3"}


def url_maker(i):
    return 'https://api.kilid.com/api/listing/search/portal/v2.0?page=' + str(i) + '&sort=kilid,DESC'


page_counter = 1
url = url_maker(page_counter)

while url:
    res = requests.post(url, json=data)
    FoundContent = res.json()['content']

    for i in range(len(FoundContent)):
        try:
            record = dict()

            record['title'] = FoundContent[i]['title']
            record['link'] = 'kilid.com/buy/' + FoundContent[i]['location']['city']['url'] + '-region' \
                             + FoundContent[i]['location']['region']['url'] \
                             + '-' + FoundContent[i]['location']['sector']['url'] + '/' \
                             + str(FoundContent[i]['id'])
            record['address'] = FoundContent[i]['location']['sector']['name']
            record['area'] = int(FoundContent[i]['floorArea'])

            print(record)
            destination_url = 'http://127.0.0.1:8000/save'
            requests.post(url=destination_url, json=record)
        except:
            pass

    page_counter += 1
    url = url_maker(page_counter)
    time.sleep(1)
