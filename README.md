<p align="center">
  <h3 align="center">database-generator</h3>
  <p align="center">
    Python Scraper
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project
Python script for scraping [fake Canadian address generator](https://www.fakeaddressgenerator.com/World/ca_address_generator) and parsing it into a customer object to insert into database.

```python
# Pick and choose which attribute to parse

URL = 'https://www.fakeaddressgenerator.com/World/ca_address_generator'

scraper = cloudscraper.create_scraper()

page = scraper.get(URL).content
soup = BeautifulSoup(page, "html.parser")
results = soup.find_all("b")

for i, result in enumerate(results):
   print(f'[{i}]: {result.text}')
  
# Sample raw scrape

[0]: BASIC INFORMATION
[1]: Clara O Barajas
[2]: female
[3]: Ms.
[4]: 10/5/1989
[5]: 274 268 465
[6]: ADDRESS
[7]: 1390 Borough Drive
[8]: Toronto
[9]: ON
[10]: Ontario
[11]: M1P 4W2
[12]: 416-290-8075
[13]: 
[..]:
[77]:

# Parse
name = results[1].text.split()
first_name = name[0]
last_name = name[2]

# Clara Barajas
full_name = first_name + " " + last_name

# Post to DB endpoint
requests.post('http://172.105.3.51:8080/api/register/customer', json = customer.scrape())
```

## Usage

```bash
./bin/python populate_db.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
