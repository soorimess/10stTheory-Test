import requests
import time


def data_maker(i):
    return "filters%5Bsort%5D%5Btitle%5D=%D8%AC%D8%AF%DB%8C%D8%AF%D8%AA%D8%B1%DB%8C%D9%86+%D9%87%D8%A7&filters%5Bsort%5D" \
       "%5Bmodel%5D=approve_time&filters%5Bsort%5D%5Border%5D=desc&filters%5Bdeal_type%5D=0&filters" \
       "%5Bdeal_type_mobile%5D=0&filters%5Bhas_tour%5D=2&filters%5Bestate_type%5D=2&filters%5Bestate_document%5D=2" \
       "&filters%5Bprice_analyse%5D=0&filters%5Bfeatures%5D%5B0%5D%5Bid%5D=1&filters%5Bfeatures%5D%5B0%5D%5Bname%5D" \
       "=%D9%BE%D8%A7%D8%B1%DA%A9%DB%8C%D9%86%DA%AF&filters%5Bfeatures%5D%5B0%5D%5Btitle%5D=parking&filters" \
       "%5Bfeatures%5D%5B0%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B1%5D%5Bid%5D=2&filters%5Bfeatures%5D%5B1%5D" \
       "%5Bname%5D=%D8%A7%D9%86%D8%A8%D8%A7%D8%B1%DB%8C&filters%5Bfeatures%5D%5B1%5D%5Btitle%5D=warehouse&filters" \
       "%5Bfeatures%5D%5B1%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B2%5D%5Bid%5D=3&filters%5Bfeatures%5D%5B2%5D" \
       "%5Bname%5D=%D8%A2%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1&filters%5Bfeatures%5D%5B2%5D%5Btitle%5D=elevator" \
       "&filters%5Bfeatures%5D%5B2%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B3%5D%5Bid%5D=4&filters%5Bfeatures%5D" \
       "%5B3%5D%5Bname%5D=%D8%A8%D8%A7%D9%84%DA%A9%D9%86&filters%5Bfeatures%5D%5B3%5D%5Btitle%5D=balcony&filters" \
       "%5Bfeatures%5D%5B3%5D%5Bstatus%5D=false&filters%5Bcenter%5D%5Blat%5D=35.73731647602422&filters%5Bcenter%5D" \
       "%5Blng%5D=51.398849487304695&filters%5Bzoom%5D=12&filters%5Bfoundation%5D%5Bmin%5D=&filters%5Bfoundation%5D" \
       "%5Bmax%5D=&filters%5Bfoundation%5D%5BminRange%5D=&filters%5Bfoundation%5D%5BmaxRange%5D=&filters%5Bprice_rent" \
       "%5D%5Bmin%5D=&filters%5Bprice_rent%5D%5Bmax%5D=&filters%5Bprice_rent%5D%5BminRange%5D=&filters%5Bprice_rent" \
       "%5D%5BmaxRange%5D=&filters%5Brahn%5D%5Bmin%5D=&filters%5Brahn%5D%5Bmax%5D=&filters%5Brahn%5D%5BminRange%5D" \
       "=&filters%5Brahn%5D%5BmaxRange%5D=&filters%5Bprice%5D%5Bmin%5D=&filters%5Bprice%5D%5Bmax%5D=&filters%5Bprice" \
       "%5D%5BminRange%5D=&filters%5Bprice%5D%5BmaxRange%5D=&filters%5Bestate_age%5D%5Bmin%5D=0&filters%5Bestate_age" \
       "%5D%5Bmax%5D=40&filters%5Bestate_age%5D%5BminRange%5D=0&filters%5Bestate_age%5D%5BmaxRange%5D=40&filters" \
       "%5Brooms%5D%5Bmin%5D=3&filters%5Brooms%5D%5Bmax%5D=3&filters%5Brooms%5D%5BminRange%5D=0&filters%5Brooms%5D" \
       "%5BmaxRange%5D=5&filters%5Bestate_floor%5D%5Bmin%5D=-1&filters%5Bestate_floor%5D%5Bmax%5D=20&filters" \
       "%5Bestate_floor%5D%5BminRange%5D=-1&filters%5Bestate_floor%5D%5BmaxRange%5D=20&filters%5Bbuilding_floors%5D" \
       "%5Bmin%5D=1&filters%5Bbuilding_floors%5D%5Bmax%5D=20&filters%5Bbuilding_floors%5D%5BminRange%5D=1&filters" \
       "%5Bbuilding_floors%5D%5BmaxRange%5D=20&filters%5Bfloor_units%5D%5Bmin%5D=1&filters%5Bfloor_units%5D%5Bmax%5D" \
       "=10&filters%5Bfloor_units%5D%5BminRange%5D=1&filters%5Bfloor_units%5D%5BmaxRange%5D=10&filters%5BleftBottom" \
       "%5D%5Blat%5D=35.61404636587197&filters%5BleftBottom%5D%5Blng%5D=51.13449096679688&filters%5BrightTop%5D%5Blat" \
       "%5D=35.86039604513405&filters%5BrightTop%5D%5Blng%5D=51.66320800781251&filters%5Bpolygon%5D=&filters" \
       "%5BeasyFilters%5D=&page=" + str(i)


url = 'https://www.melkana.com/v3/home/load-more'
headers = {'content-type': "application/x-www-form-urlencoded; charset=UTF-8", 'dnt': '1',
           'x-requested-with': 'XMLHttpRequest'}

page_counter = 1
data = data_maker(page_counter)

while data:
    res = requests.post(url=url, data=data, headers=headers)
    FoundContent = res.json()['estate_list'][0]

    try:
        record = dict()
        record['title'] = FoundContent['title']
        record['area'] = int(FoundContent['foundation'])
        record['link'] = 'https://www.melkana.com/estate/detail/' + FoundContent['code']
        record['address'] = FoundContent['some_address']

        print(record)
        destination_url = 'http://127.0.0.1:8000/save'
        requests.post(url=destination_url, json=record)
    except:
        pass

    page_counter += 1
    data = data_maker(page_counter)
    time.sleep(1)

