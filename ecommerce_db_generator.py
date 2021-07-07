# Generate customers to automatically populate database
import requests
import json

f = open('json_requests/post_register_customer.json')
prc = json.load(f)

register_customer = requests.post('http://192.168.1.59:8080/api/register/customer', json = prc)
f.close()
print(register_customer)