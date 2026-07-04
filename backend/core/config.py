from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Crypto Copilot"
    api_version: str = "0.2.0"
    api_description: str = "Backend API for AI Crypto Copilot"
    database_url: str = "sqlite:///./ai_crypto_copilot.db"
    secret_key: str = "dev-secret-key-change-later"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl_seconds: int = 60
    coingecko_api_url: str = "https://api.coingecko.com/api/v3"
    coingecko_timeout_seconds: float = 10.0
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

# Backward-compatible module-level constants
APP_NAME = settings.app_name
API_VERSION = settings.api_version
API_DESCRIPTION = settings.api_description
DATABASE_URL = settings.database_url
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes