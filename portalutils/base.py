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

        if res.status_code == 200:
            rst = res.json()
            assert 'src' in rst
            return rst['src']
        else:
            content = res.content.decode('utf-8')
            raise code2exception_mapper[res.status_code](content) \
                if res.status_code in code2exception_mapper else UnknownError(content)

    @trigger(before=_check)
    def update(self, src: str, dst: str):
        res = requests.put(urljoin(self.baseURL + '/', src), json.dumps({'dst': dst}))
        if res.status_code != 200:
            content = res.content.decode('utf-8')
            raise code2exception_mapper[res.status_code](content) \
                if res.status_code in code2exception_mapper else UnknownError(content)

    @trigger(before=_check)
    def retrieve(self, src):
        res = requests.get(urljoin(self.baseURL + '/', src), allow_redirects=False)
        if res.status_code not in (301, 302):
            content = res.content.decode('utf-8')
            raise code2exception_mapper[res.status_code](content) \
                if res.status_code in code2exception_mapper else UnknownError(content)

        return res.headers['Location']

    @trigger(before=_check)
    def delete(self, src):
        res = requests.delete(urljoin(self.baseURL + '/', src))
        if res.status_code != 200:
            content = res.content.decode('utf-8')
            raise code2exception_mapper[res.status_code](content) \
                if res.status_code in code2exception_mapper else UnknownError(content)
