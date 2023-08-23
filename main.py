import concurrent.futures
import requests
import time
from datetime import datetime
import Config
from Queue import Queue


def worker(task):
    print(f'\nstart {datetime.now()}')
    result = requests.get(task)
    print("Result = > \n", result.json())
    print(f'\nend  {datetime.now()}')


def add(queue):
    # Adding of element to queue
    for task in Config.tasks:
        queue.enqueue(task)
    return queue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q = add(Queue())
    # create a thread pool with 1 threads
    pool = concurrent.futures.ThreadPoolExecutor(Config.Config.ONE_THREAD.value)
    while not q.is_empty():
        pool.submit(worker, q.dequeue())
    time.sleep(2)
    # Section B
    print('_________________Section B________________________')
    q2 = add(Queue())

    # create a thread pool with 3 threads

    pool2 = concurrent.futures.ThreadPoolExecutor(Config.Config.NUMBER_OF_THREADS.value)
    while not q2.is_empty():
        pool2.submit(worker, q2.dequeue())
