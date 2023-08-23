import logging
from collections import deque
from Config import Config


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        if self.size() <= Config.SIZE_OF_QUEUE.value:
            self.items.append(item)
            print(f"added successfully {item} to the Queue")
        else:
            logging.warning(f" Couldn't load {item} to the Queue ,  it's Full  ")

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
