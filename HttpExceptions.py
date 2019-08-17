

class HttpStatusCodeError(BaseException):
    """
    Raised when a http request returns an invalid status code.
    Check your URL and try again!
    """
    def __init__(self, *args, **kwargs):
        raise "Error on recovering page"