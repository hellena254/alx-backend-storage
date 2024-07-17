#!/usr/bin/env python3

"""
This module contains a Cache class that provides basic Redis caching functionality.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class to interact with Redis and use it as a cache.
    """

    def __init__(self):
        """
        Initialize the Redis connection and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.
        
        :param data: Data to be stored, which can be a str, bytes, int, or float.
        :return: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
