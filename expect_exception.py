class DidNotRaise(BaseException):
    pass


class Raises:
    def __init__(self, expected_exception):
        assert issubclass(expected_exception,
                          BaseException), 'expected_exception needs to be a subclass of BaseException'
        self.expected = expected_exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.expected:
            return True
        else:
            raise DidNotRaise('expected exception was not raised')
