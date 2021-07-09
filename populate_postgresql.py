import threaded_scrape
import requests
import json

thread_count = 5

threaded_scrape.scrape(thread_count)
customer_json = 0
for i in range(0, thread_count):
    with open("json_post_data/customer%s.json" % i) as json:
        customer_json = json.load(json)
    print(requests.post('http://192.168.1.59:8080/api/register/customer', json = customer_json))

