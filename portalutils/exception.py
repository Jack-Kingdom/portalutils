"""
some user defined exception here.
"""


class CustomException(Exception):
    pass


class ArgumentsError(CustomException):
    # response status code 400
    pass


class ServerError(CustomException):
    # response status code 500
    pass


class NotFoundError(CustomException):
    # response status code 404
    pass
