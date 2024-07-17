#!/usr/bin/env python3


"""
This module contains a Cache class that provides basic Redis caching functionality,
including counting how many times its methods are called and storing the history
of inputs and outputs.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.

    :param method: The method to be decorated.
    :return: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count in Redis and calls
        the original method.

        :param self: The instance of the class.
        :param args: Positional arguments passed to the method.
        :param kwargs: Keyword arguments passed to the method.
        :return: The result of the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator to store the history of inputs and outputs for a particular function.

    :param method: The method to be decorated.
    :return: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the input arguments and output of the
        original method in Redis.

        :param self: The instance of the class.
        :param args: Positional arguments passed to the method.
        :param kwargs: Keyword arguments passed to the method.
        :return: The result of the original method.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the output
        result = method(self, *args, **kwargs)

        # Store output result
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        :param data: Data to be stored, which can be a str, bytes, int, or float.
        :return: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
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


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    :param method: The method whose history is to be displayed.
    """
    redis_instance = method.__self__._redis
    method_key = method.__qualname__

    input_key = f"{method_key}:inputs"
    output_key = f"{method_key}:outputs"

    input_list = redis_instance.lrange(input_key, 0, -1)
    output_list = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_key} was called {len(input_list)} times:")

    for inp, out in zip(input_list, output_list):
        print(f"{method_key}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")
