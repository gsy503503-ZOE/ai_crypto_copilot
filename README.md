# AI Crypto Copilot

AI Crypto Copilot is an AI-powered research assistant for crypto investors and builders.

## Goal

Build a practical AI product that helps users analyze crypto market data, wallet activity, news, and portfolio signals.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- OpenAI API

## Current Status

v0.2 is complete.

Completed:

- FastAPI backend foundation
- User authentication with JWT
- Crypto market data endpoints via CoinGecko
- Redis caching with in-memory fallback
- Docker Compose setup
- GitHub Actions CI
- Environment-based configuration

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/gsy503503-ZOE/ai_crypto_copilot.git
cd ai_crypto_copilot
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
```

### 5. Initialize the database

```bash
python -m backend.db.init_db
```

### 6. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 7. Run tests

```bash
pytest -q
```

### 8. Run with Docker Compose

```bash
docker compose up --build
```

## API Endpoints

Root endpoint:

```text
http://127.0.0.1:8000/
```

Health check:

```text
http://127.0.0.1:8000/health
```

Auth:

```text
POST /auth/register
POST /auth/login
GET  /auth/me
```

Market data:

```text
GET /v1/market/price/bitcoin
GET /v1/market/prices?ids=bitcoin,ethereum
GET /v1/market/trending
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Roadmap

- v0.0.1 Backend foundation
- v0.1 User authentication
- v0.2 Crypto market data
- v0.3 Wallet analysis
- v0.4 AI research assistant