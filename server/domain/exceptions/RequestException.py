class RequestException(Exception):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
