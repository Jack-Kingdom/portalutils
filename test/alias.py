import unittest
from portalutils import alias
from portalutils.exception import ArgumentsError, NotFoundError


class AliasTest(unittest.TestCase):

    def test_create(self):
        k, v = 'key', 'http://example.com'

        src = alias.create(k, v)
        self.assertIsInstance(src, str)
        alias.delete(k)

    def test_illegal_create(self):
        k, v = 'key', 'example'
        with self.assertRaises(ArgumentsError):
            alias.create(k, v)

    def test_update(self):
        k = 'key'
        url = "https://example.com"
        new_url = "https://google.com"

        src = alias.create(k, url)
        self.assertEqual(alias.retrieve(src), url)
        alias.update(src, new_url)
        self.assertEqual(alias.retrieve(src), new_url)

        alias.delete(k)

    def test_retrieve(self):
        k = 'key'
        url = "https://google.com"
        src = alias.create(k, url)
        dst = alias.retrieve(src)
        self.assertEqual(dst, url)
        alias.delete(k)

    def test_delete(self):
        k = 'key'
        url = "https://google.com"

        src = alias.create(k, url)
        self.assertEqual(alias.retrieve(src), url)

        alias.delete(src)
        with self.assertRaises(NotFoundError):
            alias.retrieve(src)
