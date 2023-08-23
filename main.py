import concurrent.futures
import requests
import time
from datetime import datetime
from Queue import Queue


def worker(task):
    print(f'\nstart {datetime.now()}')
    result = requests.get(task)
    print("Result = > \n", result.json())
    print(f'\nend  {datetime.now()}')


def add(queue):
    # Adding of element to queue
    queue.enqueue("https://jsonplaceholder.typicode.com/posts/1")
    queue.enqueue("https://jsonplaceholder.typicode.com/todos/1")
    queue.enqueue("https://jsonplaceholder.typicode.com/users/1")
    return queue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q = add(Queue())
    q2 = add(Queue())
    # create a thread pool with 1 threads
    pool = concurrent.futures.ThreadPoolExecutor(1)
    while not q.is_empty():
        pool.submit(worker, q.dequeue())
    time.sleep(2)
    # Section B
    print('_________________Section B________________________')
    # create a thread pool with 3 threads

    pool2 = concurrent.futures.ThreadPoolExecutor(3)
    while not q2.is_empty():
        pool2.submit(worker, q2.dequeue())
