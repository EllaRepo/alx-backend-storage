#!/usr/bin/env python3
"""This module defines a class Cache
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """A Cache class
    """
    def __init__(self) -> None:
        """Initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string
        Args:
            data: input data
        Returns:
            the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """Get data from redis cache
        """
        value = self._redis.get(key)
        if value is not None and fn is not None and callable(fn):
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get data as string from redis cache
        Args:
            key (str): key
        Returns:
            str: data
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get data as integer from redis cache
        Args:
            key (str): key
        Returns:
            int: data
        """
        return self.get(key, fn=int)
