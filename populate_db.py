from concurrent.futures import ThreadPoolExecutor

import customer
import requests
import json
import time


def cus_cnt():
    raw_json = requests.get('http://172.105.3.51:8080/api/customers/list/customers')
    print(f'Customer count: {len(json.loads(raw_json.text))}')


def task():
    requests.post('http://172.105.3.51:8080/api/register/customer', json=customer.main())


def main():
    executor = ThreadPoolExecutor(max_workers=8)

    i = 0
    while True:
        if i == 1000:
            i = 0
            cus_cnt()
        executor.submit(task)
        time.sleep(0.002)
        i += 1


if __name__ == '__main__':
    main()
