import json
from urllib.parse import urljoin
import requests
from .exception import *
from .utils import trigger
from .config import Configure


class Base(object):
    def __init__(self, key):
        self.baseURL = Configure().get(key)

    def _check(self, *args, **kwargs):
        if not self.baseURL:
            raise RuntimeError('baseURL must init and supplied')

    @trigger(before=_check)
    def create(self, *args):
        if len(args) == 1:
            dst, = args
            res = requests.post(self.baseURL, json.dumps({'dst': dst}))
        elif len(args) == 2:
            src, dst = args
            res = requests.post(self.baseURL, json.dumps({'src': src, 'dst': dst}))
        else:
            raise RuntimeError('args too many.')

        if res.status_code == 400:
            raise ArgumentsError(res.content)
        else:
            assert res.status_code == 200
            rst = res.json()
            assert 'src' in rst
            return rst['src']

    @trigger(before=_check)
    def update(self, src, dst):

        res = requests.put(urljoin(self.baseURL + '/', src), json.dumps({'dst': dst}))

    @trigger(before=_check)
    def retrieve(self, src):

        res = requests.get(urljoin(self.baseURL + '/', src))

    @trigger(before=_check)
    def delete(self, src):

        res = requests.put(urljoin(self.baseURL + '/', src))
