from concurrent.futures import ThreadPoolExecutor

import scrape_customer_and_login
import requests
import json
import time


# Set email restriction to 10 variations "Abbott_Kim{n}" n < 10

# def cus_cnt():
#     raw_json = requests.get('http://localhost:8080/api/customer/list')
#     print(f'Customer count: {len(json.loads(raw_json.text))}')


def task():
    customer, login = scrape_customer_and_login.main()

    requests.post('http://localhost:8080/api/customer/add', json=customer)

    requests.post('http://localhost:8080/api/login/add', json=login)


def main():
    executor = ThreadPoolExecutor(max_workers=8)

    i = 0
    while True:
        # if i == 1000:
        #     i = 0
            # cus_cnt()
        executor.submit(task)
        time.sleep(0.002)
        i += 1


if __name__ == '__main__':
    main()
