import unittest

import requests

import Config
from Queue import Queue
from main import worker, addTasks

posts = "https://jsonplaceholder.typicode.com/posts/1"
todo = "https://jsonplaceholder.typicode.com/todos/1"
users = "https://jsonplaceholder.typicode.com/users/1"


class Testing(unittest.TestCase):

    def test_getPosts(self):
        self.assertEqual(requests.get(posts).status_code, 200)

    def test_getTodo(self):
        self.assertEqual(requests.get(todo).status_code, 200)

    def test_getUser(self):
        self.assertEqual(requests.get(users).status_code, 200)

    def test_emptyQueue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(posts)

    def test_workerFunction(self):
        q = Queue()
        self.assertEqual(worker(Config.Config.USERS.value),200)
        q.enqueue(posts)

    def test_addTasksFunction(self):
        q = addTasks(Queue())
        self.assertEqual(q.size(),Config.Config.SIZE_OF_QUEUE.value)




if __name__ == '__main__':
    unittest.main()
