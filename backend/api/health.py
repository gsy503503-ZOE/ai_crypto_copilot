from fastapi import APIRouter

from backend.cache import cache
from backend.core.config import API_VERSION

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": API_VERSION,
        "cache": cache.backend_name,
    }