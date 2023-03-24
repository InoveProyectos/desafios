#!/usr/bin/env python

from redis import Redis as RedisClient
from ...config.environment import *

class Redis:
    def __init__(self):
        self._redis = RedisClient(
            host=connections['redis']['host'], 
            port=connections['redis']['port'], 
            db=connections['redis']['db'], 
            password=connections['redis']['password'],
            decode_responses=True)
    
    def exists(self, key):
        return self._redis.exists(key)
    
    def get(self, key):
        return self._redis.get(key)
    
    def set(self, key, value, ttl:int=ttl):
        """
        ttl: time to live in seconds
        """
        return self._redis.set(key, value, ex=connections['redis']['ttl'])
    
    def delete(self, key):
        return self._redis.delete(key)
