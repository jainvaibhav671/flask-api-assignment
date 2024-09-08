from typing import Dict
import time

from ..constants import CACHE_EXPIRATION_TIME


class Cache:
    def __init__(self):
        self.cache: Dict[str, Dict] = dict()

    def add(self, key: str, value):
        self.cache[key] = {
            "data": value,
            "timestamp": time.time()
        }

    def get(self, key: str):
        if key not in self.cache:
            return None

        item = self.cache[key]
        if not self.is_expired(item["timestamp"]):
            return item["data"]
        else:
            del self.cache[key]

    def is_expired(self, timestamp):
        diff = time.time() - timestamp
        return diff >= CACHE_EXPIRATION_TIME
