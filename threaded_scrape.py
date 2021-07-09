# Generate customers to automatically populate database
import concurrent.futures
import fake_address_generator_scrape
# import logging

# print(register_customer)

def thread_function(thread):
    # logging.info("Thread %s: starting", thread)
    fake_address_generator_scrape.scrape(thread)
    # logging.info("Thread %s: finishing", thread)


def scrape(thread_number):
    format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_number) as executer:
        executer.map(thread_function, range(thread_number))