# https://www.fakeaddressgenerator.com/World/ca_address_generator

import cloudscraper
import threading
from bs4 import BeautifulSoup

URL = 'https://www.fakeaddressgenerator.com/World/ca_address_generator'

scraper = cloudscraper.create_scraper()

"""def getPerson():
    threading.Timer(6, getPerson).start()
    page = scraper.get(URL).content
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find_all("b")
    print(results[1].text.strip())"""

# getPerson()

page = scraper.get(URL).content
soup = BeautifulSoup(page, "html.parser")
results = soup.find_all("b")

name = results[1].text.split()
first_name = name[0]
print('first_name: ', first_name)
last_name = name[2]
print('last_name: ', last_name)
full_name = first_name + " " + last_name
print('full_name: ', full_name)

phone_number = results[12].text
phone_number = phone_number.split("-")[0]+phone_number.split("-")[1]+phone_number.split("-")[2]
print('phone_number: ', phone_number)

email = results[52].text + "@gmail.com"
print('email: ', email)

password = results[53].text
print('password: ', password)

date_of_birth = results[4].text

if (len(date_of_birth.split("/")[0]) == 1):
    day = "0" + date_of_birth.split("/")[0]
else:
    day = date_of_birth.split("/")[0]

if (len(date_of_birth.split("/")[1]) == 1):
    month = "0" + date_of_birth.split("/")[1]
else:
    month = date_of_birth.split("/")[1]

date_of_birth = (date_of_birth.split("/")[2][2] + date_of_birth.split("/")[2][3]) + month + day
print('date_of_birth: ', date_of_birth)

street_name = results[7].text.split()[1] + " " + results[7].text.split()[2]
print('street_name: ', street_name)

street_number = results[7].text.split()[0]
print('street_number: ', street_number)

city = results[8].text
print('city: ', city)

postal_code = results[11].text.split()[0] + results[11].text.split()[1]
print('postal_code: ', postal_code)

province = results[10].text
print('province: ', province)

ccn = results[30].text
print('ccn: ', ccn)

four_dig = ccn[12] + ccn[13] + ccn[14] + ccn [15]
print('four_dig: ', four_dig)

cvc = results[31].text
print('cvc: ', cvc)

customer = {
    "firstName": first_name,
    "lastName": last_name,
    "phoneNumber": phone_number,
    "email": email,
    "password": password,
    "dateOfBirth": date_of_birth,
    "address": {
        "streetName": street_name,
        "streetNumber": street_number,
        "unitNumber": 000,
        "city": city,
        "postalCode": postal_code,
        "province": province
    },
    "cart": {
        "items": [
            {
                "itemName": "productName",
                "description": "description",
                "price": 34.65
            }
        ],
        "customerEmail": email,
        "total": 34.65
    },
    "creditCards": [
        {
            "fullName": full_name,
            "ccn": ccn,
            "expDate": "0425",
            "cvc": cvc,
            "fourDig": four_dig
        }
    ],
    "orders": [
        {
            "orderStatus": "orderStatus",
            "customerEmail": "customerEmail",
            "order": [
                {
                    "itemName": "productName",
                    "description": "description",
                    "price": 34.65
                }
            ],
            "totalPrice": 34.65
        }
    ]
}

"""i = 0
for b_ele in results:
    print(f'b_ele[{i}]: {b_ele.text}')
    i += 1"""


