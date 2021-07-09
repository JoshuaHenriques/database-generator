import fake_address_generator_scrape
import requests
import time


i = 0
while(True):
    customer_json = fake_address_generator_scrape.scrape()
    response = requests.post('http://192.168.1.59:8080/api/register/customer', json = customer_json)
    print(response)
    print(response.text)
    i += 1
    time.sleep(6)

