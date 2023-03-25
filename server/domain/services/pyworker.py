#!/usr/bin/env python

from .service import Service
from ...config.environment import *

class Pyworker(Service):
    def __init__(self):
        super().__init__(workers["pyworker"]["url"])

    def test(self, body):
        """
        body: {
            "code": str,
            "inputs": str
        }
        """ 
        return self.post("/test", body=body)
    
    def run(self, body):
        return self.post("/run-code", body=body)