import unittest

import requests
from Queue import Queue

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




if __name__ == '__main__':
    unittest.main()
