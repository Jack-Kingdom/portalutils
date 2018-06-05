#! bin/python
"""
configure store
"""

from .utils import SingletonDecorator


@SingletonDecorator
class Configure(object):

    def __init__(self):
        self.store = {
            'alias': 'http://localhost:8888/api/v1/alias',
            'shortURL': 'http://localhost:8888/api/v1/shortURL',
        }

    def register(self, key: str, value: str):
        if key not in self.store:
            raise IndexError('key not in configure')

        self.store[key] = value

    def get(self, key: str):
        if key not in self.store:
            raise IndexError('key not in configure')

        return self.store[key]
