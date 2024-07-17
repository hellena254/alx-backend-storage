#!/usr/bin/env python3


"""
This module contains a function to fetch and cache web pages using Redis.
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """
    Decorator to count the number of requests made to a particular URL.

    :param method: The method to be decorated.
    :return: The wrapped method.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that increments the request count and calls
        the original method.

        :param url: The URL to fetch.
        :return: The HTML content of the URL.
        """
        r.incr(f"count:{url}")
        return method(url)
    
    return wrapper

def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the HTML content of a URL in Redis.

    :param method: The method to be decorated.
    :return: The wrapped method.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that caches the HTML content of the URL.

        :param url: The URL to fetch.
        :return: The HTML content of the URL.
        """
        cached_page = r.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')
        
        page = method(url)
        r.setex(f"cached:{url}", 10, page)
        return page
    
    return wrapper

@count_requests
@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a particular URL and cache the result with an
    expiration time of 10 seconds.

    :param url: The URL to fetch.
    :return: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
