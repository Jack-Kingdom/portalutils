import unittest
from portalutils import shortURL
from portalutils.exception import ArgumentsError, NotFoundError


class ShortURLTest(unittest.TestCase):

    def test_create(self):
        allowed_url = ('http://example.com', 'https://google.com')

        for url in allowed_url:
            src = shortURL.create(url)
            self.assertIsInstance(src, str)

    def test_illegal_create(self):
        illegal_url = ('example', 'hello')

        for url in illegal_url:
            with self.assertRaises(ArgumentsError):
                shortURL.create(url)

    def test_update(self):
        url = "https://example.com"
        new_url = "https://google.com"

        src = shortURL.create(url)
        self.assertEqual(shortURL.retrieve(src), url)
        shortURL.update(src, new_url)
        self.assertEqual(shortURL.retrieve(src), new_url)

    def test_retrieve(self):
        url = "https://google.com"
        src = shortURL.create(url)
        dst = shortURL.retrieve(src)
        self.assertEqual(dst, url)

    def test_delete(self):
        url = "https://google.com"

        src = shortURL.create(url)
        self.assertEqual(shortURL.retrieve(src), url)

        shortURL.delete(src)
        with self.assertRaises(NotFoundError):
            shortURL.retrieve(src)
