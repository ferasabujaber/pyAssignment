import concurrent.futures
import logging
import requests
import time
from datetime import datetime
import Config
from Queue import Queue


def worker(url):
    print(f'\n Start time todo a task  {datetime.now()}')
    # http request get
    result = requests.get(url)
    print(" Result = >  ", result.json())
    print(f' The task was completed successfully at  {datetime.now()}')
    return result.status_code


def addTasks(queue):
    print("add tasks to the Queue in progress")
    # Adding of element to queue
    if len(Config.tasks) < Config.Config.SIZE_OF_QUEUE.value:
        logging.warning("Be careful , didn't put enough tasks in the queue !!!")
    for task in Config.tasks:
        time.sleep(0.2)
        queue.enqueue(task)
    print("Add tasks to the queue completed")

    return queue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q = addTasks(Queue())
    # create a thread pool with 1 threads
    pool = concurrent.futures.ThreadPoolExecutor(Config.Config.ONE_THREAD.value)
    while not q.is_empty():
        pool.submit(worker, q.dequeue())
    time.sleep(2)
    # Section B
    print('_________________Section B________________________')
    q2 = addTasks(Queue())

    # create a thread pool with 3 threads

    pool2 = concurrent.futures.ThreadPoolExecutor(Config.Config.NUMBER_OF_THREADS.value)
    while not q2.is_empty():
        pool2.submit(worker, q2.dequeue())
