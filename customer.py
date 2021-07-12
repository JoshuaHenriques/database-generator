from bs4 import BeautifulSoup
import cloudscraper


def main():
    url = 'https://www.fakeaddressgenerator.com/World/ca_address_generator'

    scraper = cloudscraper.create_scraper()

    page = scraper.get(url).content
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find_all("b")

    name = results[1].text.split()
    first_name = name[0]
    last_name = name[2]
    full_name = first_name + " " + last_name

    phone_number = results[12].text
    phone_number = phone_number.split("-")[0] + phone_number.split("-")[1] + phone_number.split("-")[2]

    email = last_name + "_" + first_name + phone_number[8] + phone_number[9] + "@gmail.com"

    password = results[53].text

    date_of_birth = results[4].text

    if len(date_of_birth.split("/")[0]) == 1:
        day = "0" + date_of_birth.split("/")[0]
    else:
        day = date_of_birth.split("/")[0]

    if len(date_of_birth.split("/")[1]) == 1:
        month = "0" + date_of_birth.split("/")[1]
    else:
        month = date_of_birth.split("/")[1]

    date_of_birth = (date_of_birth.split("/")[2][2] + date_of_birth.split("/")[2][3]) + month + day

    street_name = results[7].text.split()[1] + " " + results[7].text.split()[2]

    street_number = results[7].text.split()[0]

    city = results[8].text

    postal_code = results[11].text.split()[0] + results[11].text.split()[1]

    province = results[10].text

    ccn = results[30].text

    four_dig = ccn[12] + ccn[13] + ccn[14] + ccn[15]

    cvc = results[31].text

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
        "cart": {},
        "creditCards": [
            {
                "fullName": full_name,
                "ccn": ccn,
                "expDate": "0425",
                "cvc": cvc,
                "fourDig": four_dig
            }
        ],
        "orders": []
    }

    return customer


if __name__ == "__main__":
    main()
