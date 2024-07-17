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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        :param key: The key to retrieve the data for.
        :param fn: Optional callable to convert the data back to the desired format.
        :return: The data stored in Redis, optionally converted using fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        :param key: The key to retrieve the data for.
        :return: The data stored in Redis, decoded as a UTF-8 string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))


    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        :param key: The key to retrieve the data for.
        :return: The data stored in Redis, converted to an integer.
        """
        return self.get(key, lambda d: int(d))
