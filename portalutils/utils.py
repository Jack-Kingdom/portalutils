"""
some utilities, decorators in this file.
"""
import functools


class SingletonDecorator(object):
    """
    class decorator, wrap class to singleton
    """

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


def trigger(before=None, after=None):
    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            [m(*args, **kwargs) for m in iter(before)] if before else None
            rst = func(*args, **kwargs)
            [m(*args, **kwargs) for m in iter(after)] if after else None

            return rst

        return inner_wrapper

    return wrapper
