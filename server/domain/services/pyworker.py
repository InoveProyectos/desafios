#!/usr/bin/env python

from .service import Service
from ...config import *

class Pyworker(Service):
    def __init__(self):
        super().__init__(workers["pyworker"]["url"])

    def test(self, code: str, inputs: str = None):
        return self.post("/test", body=dict(code, inputs))
    
    def run_code(self, files, tests, clean_db=False, encapsulate_in_fn=False,avoid_main=False):
        return self.post("/run-code", body=dict(files=files, tests=tests, clean_db=clean_db, encapsulate_in_fn=encapsulate_in_fn,avoid_main=avoid_main))
