#!/usr/bin/env python

from .service import Service
from ...config.environment import *

class Pyworker(Service):
    def __init__(self):
        super().__init__(workers["pyworker"]["url"])

    def test(self, code: str, inputs: str = None):
        return self.post("/test", body=dict(code, inputs))
    
    def run(self, files, tests, repository=""):
        return self.post("/run-code", body=dict(files=files, tests=tests, repository=repository))
