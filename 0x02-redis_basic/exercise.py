#!/usr/bin/env python3
"""
Has a class definition for redis cache
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Defines methods to handle redis cache operations
    """
    def __init__(self) -> None:
        """
        Initialize redis client
        Attributes:
            self._redis (redis.Redis): redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis cache
        Args:
            data (dict): data to store
        Returns:
            str: key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
