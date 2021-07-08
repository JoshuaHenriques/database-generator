# https://www.fakeaddressgenerator.com/World/ca_address_generator

import requests
import cloudscraper

f = open('gen0.html', 'w')

URL = 'https://www.fakeaddressgenerator.com/World/ca_address_generator'

scraper = cloudscraper.create_scraper()
page = scraper.get(URL).text

f.write(page)