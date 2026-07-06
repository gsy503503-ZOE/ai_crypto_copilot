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

Current release: `v0.2.0`

Completed:

- Backend foundation with FastAPI
- User registration and login
- Password hashing with Passlib and bcrypt
- JWT access token authentication
- Protected current user endpoint
- Crypto market data endpoints
- Real market price lookup with CoinGecko
- Market summary endpoint
- Sprint documentation and GitHub releases

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

### 4. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 5. Open the API

Root endpoint:

```text
http://127.0.0.1:8000/
```

Health check:

```text
http://127.0.0.1:8000/health
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Roadmap

- v0.0.1 Backend foundation - completed
- v0.1.0 User authentication - completed
- v0.2.0 Crypto market data - completed
- v0.3.0 Wallet analysis - planned
- v0.4.0 AI research assistant - planned

## Current Features

- User registration and login
- Password hashing with Passlib and bcrypt
- JWT access token authentication
- Protected current user endpoint
- Crypto coin list endpoint
- Real-time coin price lookup with CoinGecko
- Market summary endpoint for BTC, ETH, and SOL