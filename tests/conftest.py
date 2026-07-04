import pytest
from fastapi.testclient import TestClient

from backend.cache.redis_cache import MemoryCache
from backend.main import app
import backend.cache.redis_cache as cache_module


@pytest.fixture(autouse=True)
def reset_cache_backend():
    cache_module.cache.backend = MemoryCache()
    cache_module.cache.backend_name = "memory"
    yield


@pytest.fixture
def client():
    return TestClient(app)