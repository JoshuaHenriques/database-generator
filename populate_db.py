from concurrent.futures import ThreadPoolExecutor

import threading
import fake_address_generator_scrape
import requests
import json
import time

def cus_cnt():
    raw_json = requests.get('http://172.105.3.51:8080/api/customers/list/customers')
    print(f'\n************************\nCustomer count: {len(json.loads(raw_json.text))}\n************************\n')

def task():
    customer_json = fake_address_generator_scrape.scrape()
    response = requests.post('http://172.105.3.51:8080/api/register/customer', json = customer_json)
    print(response)
    print("Task Executed {}".format(threading.current_thread()))

def main():
    executor = ThreadPoolExecutor(max_workers=8)
    
    i = 0
    while(True):
        if i == 3000:
            i = 0
            cus_cnt()
        executor.submit(task)
        time.sleep(0.002)
        i += 1


if __name__ == '__main__':
    main()