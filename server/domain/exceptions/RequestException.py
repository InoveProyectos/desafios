class RequestException(Exception):
    def __init__(self, msg, **kwargs):
        super().__init__(msg)
        self.__dict__.update(kwargs)
