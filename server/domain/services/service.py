#!/usr/bin/env python

import requests

class Service:
    def __init__(uri, access_token="", api_path="/api", auth_prefix="Bearer", auth_header="Authorization"):
        self.uri = uri
        self.access_token = access_token
        self.api_path = api_path
        self.auth_prefix = auth_prefix + " "
        self.auth_header = auth_header
    
    def _request(method="get", path: str, qs: dict = None, body: dict = None)
        base_url = self.uri + self.api_path + path
        headers = {
            self.auth_header: self.auth_prefix + self.access_token
        }
        return requests.request(method, base_url, params=qs, json=body, headers=headers)

    def get(path: str, qs: dict = None):
        return self._request("get", path, qs)

    def post(path: str, body: dict = None):
        return self._request("post", path, body=body)
    
    def put(path: str, body: dict = None):
        return self._request("put", path, body=body)
    
    def patch(path: str, body: dict = None):
        return self._request("patch", path, body=body)
    
    def delete(path: str, qs: dict = None):
        return self._request("delete", path, qs)