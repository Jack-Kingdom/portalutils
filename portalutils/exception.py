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


class UnknownError(CustomException):
    pass


code2exception_mapper = {
    400: ArgumentsError,
    404: NotFoundError,
    500: ServerError,
}