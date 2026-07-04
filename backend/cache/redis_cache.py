import json
import time
from typing import Any

import redis

from backend.core.config import settings


class CacheBackend:
    def get(self, key: str) -> Any | None:
        raise NotImplementedError

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        raise NotImplementedError

    def ping(self) -> bool:
        return True


class MemoryCache(CacheBackend):
    def __init__(self) -> None:
        self._store: dict[str, tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        item = self._store.get(key)
        if item is None:
            return None
        expires_at, value = item
        if expires_at < time.time():
            self._store.pop(key, None)
            return None
        return value

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        self._store[key] = (time.time() + ttl_seconds, value)


class RedisCache(CacheBackend):
    def __init__(self, redis_url: str) -> None:
        self.client = redis.Redis.from_url(redis_url, decode_responses=True)

    def get(self, key: str) -> Any | None:
        raw = self.client.get(key)
        if raw is None:
            return None
        return json.loads(raw)

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        self.client.setex(key, ttl_seconds, json.dumps(value))

    def ping(self) -> bool:
        return bool(self.client.ping())


class HybridCache:
    def __init__(self) -> None:
        self.backend: CacheBackend = MemoryCache()
        self.backend_name = "memory"
        self._connect_redis()

    def _connect_redis(self) -> None:
        try:
            candidate = RedisCache(settings.redis_url)
            if candidate.ping():
                self.backend = candidate
                self.backend_name = "redis"
        except (redis.RedisError, OSError):
            self.backend = MemoryCache()
            self.backend_name = "memory"

    def get(self, key: str) -> Any | None:
        return self.backend.get(key)

    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        self.backend.set(key, value, ttl_seconds or settings.cache_ttl_seconds)

    def is_redis_connected(self) -> bool:
        return self.backend_name == "redis"


cache = HybridCache()