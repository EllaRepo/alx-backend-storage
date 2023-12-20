#!/usr/bin/env python3
"""This module defines a get_page
"""
import redis
import requests
from datetime import timedelta
from functools import wraps


def track_request_count(func):
    """Decorator to track request count for a URL
    """
    @wraps(func)
    def wrapper(url):
        redis_store = redis.Redis()
        req_key = f'count:{url}'
        redis_store.incr(req_key)
        return func(url)
    return wrapper

def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML
       content of a particular URL and returns it
    """
    if url is None or len(url.strip()) == 0:
        return ''

    redis_store = redis.Redis()
    res_key = f'result:{url}'
    result = redis_store.get(res_key)

    if result is not None:
        return result.decode('utf-8')

    result = requests.get(url).content.decode('utf-8')

    redis_store.setex(res_key, timedelta(seconds=10), result)

    return result
