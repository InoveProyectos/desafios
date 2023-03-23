#!/usr/bin/env python

from .service import Service

class PyworkerService(Service):
    def __init__(self):
        super().__init__(pyworker["url"])

    def test(body):
        """
        body: {
            "code": str,
            "inputs": str
        }
        """ 
        return self.post("/test", body=body)
    
    def run(body):
        return self.post("/run-code", body={"code": code, "inputs": inputs})