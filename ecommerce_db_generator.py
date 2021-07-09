# Generate customers to automatically populate database
import requests
# f = open('json_requests/post_register_customer.json')
# prc = json.load(f)
# print(prc['firstName'])
# f.close()

# register_customer = requests.post('http://192.168.1.59:8080/api/register/customer', json = prc)
# print(register_customer)

# api.name-fake.com/english-united-states/female/ 

# Useful fields: name, address, birth_data, phone_h, email_u, email_d, username, password, uuid
json_response = requests.get('https://api.namefake.com/').json()

name = json_response['name']
_first_name = name.split()[0]

chars = [char for char in _first_name] 
# print(chars)

if chars[len(chars) - 1] == '.':
    first_name = name.split()[1]
    second_name = name.split()[2]
else:
    first_name = name.split()[0]
    second_name = name.split()[1]

# print(first_name)
# print(second_name)

address = json_response['address']
# print(f'address:\n', address)

address_split = address.split()
# print(f'address.split():', address_split)

# print(f'len(address_split): ', len(address_split))

street_number = address_split[0]
# print(f'street_number:', street_number)

street_name = address_split[1]+' '+address_split[2]
# print(f'street_name:', street_name)

zipcode = address_split[len(address_split) - 1]
# print(f'zipcode: ', zipcode)

state = address_split[len(address_split) - 2]
# print(f'state: ', state)

city = address_split[len(address_split) - 3]
city_chars = [char for char in city]
city_chars.remove(',')
city = ''

for char in city_chars:
    city += char

# print(f'city: ', city)

birth_data = json_response['birth_data']
print(f'birth_date: ', birth_data)

phone_h = json_response['phone_h']
email = json_response['email_u'] + json_response['email_d']
username = json_response['username']
password = json_response['password']
uuid = json_response['uuid']