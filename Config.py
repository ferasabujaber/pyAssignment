from enum import Enum


class Config(Enum):
    SIZE_OF_QUEUE = 3
    ONE_THREAD = 1  # Section A
    NUMBER_OF_THREADS = 3  # Section B
    POSTS = "https://jsonplaceholder.typicode.com/posts/1"
    TODO = "https://jsonplaceholder.typicode.com/todos/1"
    USERS = "https://jsonplaceholder.typicode.com/users/1"


tasks = [Config.POSTS.value, Config.TODO.value, Config.USERS.value]
