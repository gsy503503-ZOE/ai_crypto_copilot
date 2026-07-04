# Sprint 2 Review: Crypto Market Data

## Sprint Goal

Deliver v0.2 crypto market data endpoints with caching, environment-based configuration, CORS, Docker support, and automated tests.

By the end of Sprint 2, the backend can:

- Return a single coin price
- Return multiple coin prices
- Return trending coins
- Cache market responses in Redis with in-memory fallback
- Run in Docker Compose with Redis
- Expose versioned `/v1/market` routes

## Completed Work

### 1. Environment Configuration

- Migrated settings to `pydantic-settings`
- Added `.env.example` for local setup
- Centralized Redis, CoinGecko, and CORS settings in `backend/core/config.py`

### 2. Market Data Service

- Added `backend/services/coingecko.py`
- Integrated CoinGecko public API for prices and trending coins
- Added typed response schemas in `backend/schemas/market.py`

### 3. Market API Endpoints

- `GET /v1/market/price/{coin_id}`
- `GET /v1/market/prices?ids=bitcoin,ethereum`
- `GET /v1/market/trending`

### 4. Caching Layer

- Added `backend/cache/redis_cache.py`
- Redis cache in production/docker
- In-memory fallback for local development without Redis
- Health endpoint now reports cache backend

### 5. Platform Hardening

- Added CORS middleware for future frontend work
- Added Dockerfile and `docker-compose.yml`
- Added GitHub Actions CI workflow
- Added pytest coverage for auth, health, and market routes

## Testing

Verified with pytest:

- Health endpoint returns version `0.2.0`
- Market endpoints return expected payload shapes
- Cache flag switches to `true` on repeated requests
- Auth flow still works after config refactor

## Sprint 2 Result

The project moved from authentication-only backend to the first real crypto data feature slice. v0.2 is ready for frontend integration and wallet analysis in v0.3.