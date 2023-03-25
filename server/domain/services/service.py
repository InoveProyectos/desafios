#!/usr/bin/env python

import requests

class Service:
    def __init__(self, uri, access_token="", api_path="/api", auth_prefix="Bearer", auth_header="Authorization"):
        self.uri = uri
        self.access_token = access_token
        self.api_path = api_path
        self.auth_prefix = auth_prefix + " "
        self.auth_header = auth_header


    def _request(self, method: str, path: str, qs: dict = None, body: dict = None):
        base_url = self.uri + self.api_path + path
        headers = {
            self.auth_header: self.auth_prefix + self.access_token
        }
        return requests.request(method, base_url, params=qs, json=body, headers=headers)


    def get(self, path: str, qs: dict = None):
        return self._request("get", path, qs)


    def post(self, path: str, body: dict = None):
        return self._request("post", path, body=body)


    def put(self, path: str, body: dict = None):
        return self._request("put", path, body=body)


    def patch(self, path: str, body: dict = None):
        return self._request("patch", path, body=body)


    def delete(self, path: str, qs: dict = None):
        return self._request("delete", path, qs)
