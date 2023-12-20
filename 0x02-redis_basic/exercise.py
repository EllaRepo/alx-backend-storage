#!/usr/bin/env python3
"""This module defines a class Cache
"""
import redis
import uuid
from typing import Union


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
