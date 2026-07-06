# AI Crypto Copilot

AI Crypto Copilot is an AI-powered research assistant for crypto investors and builders.

## Goal

Build a practical AI product that helps users analyze crypto market data, wallet activity, news, and portfolio signals.

## Current Status

Current version: v0.3.0 in progress

Sprint 3 focuses on wallet analysis. The backend can now validate EVM wallet addresses, return mock wallet analysis, calculate wallet risk signals, and generate readable wallet insights.

Completed:

- Backend foundation with FastAPI
- User registration and login
- Password hashing with Passlib and bcrypt
- JWT access token authentication
- Protected current user endpoint
- Crypto market data endpoints
- Real market price lookup with CoinGecko
- Market summary endpoint
- Wallet address validation
- Mock wallet analysis
- Wallet risk level and risk score calculation
- Wallet activity level detection
- Wallet insight generation
- Wallet service smoke checks
- Sprint documentation and GitHub releases

## Tech Stack

Currently used:

- Python
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy
- Pydantic
- Passlib
- bcrypt
- python-jose
- httpx
- CoinGecko API

Planned:

- PostgreSQL
- Redis
- Docker
- OpenAI API

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

### 4. Initialize the database

```bash
python -m backend.db.init_db
```

### 5. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 6. Open the API

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
- v0.3.0 Wallet analysis - in progress
- v0.4.0 AI research assistant - planned

## Current Features

### Authentication

- User registration
- User login
- Password hashing with Passlib and bcrypt
- JWT access token generation
- Protected current user endpoint

### Market Data

- Crypto coin list endpoint
- Real-time coin price lookup with CoinGecko
- Market summary endpoint for BTC, ETH, and SOL
- Mock fallback data when external market data is unavailable

### Wallet Analysis

- EVM wallet address validation
- Wallet analysis endpoint
- Mock wallet transaction data
- Risk level calculation
- Risk score calculation
- Activity level detection
- Human-readable wallet insights
- Analysis timestamp

## API Endpoints

### Health

- `GET /`
- `GET /health`

### Authentication

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### Market

- `GET /market/coins`
- `GET /market/coins/{symbol}/price`
- `GET /market/summary`

### Wallet

- `GET /wallet/ping`
- `POST /wallet/analyze`

## Example Wallet Analysis Request

```json
{
  "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
}
```

## Example Wallet Analysis Response

```json
{
  "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
  "risk_level": "low",
  "risk_score": 5,
  "activity_level": "medium",
  "total_transactions": 128,
  "analyzed_at": "2026-07-06T10:25:30.123456",
  "insights": [
    {
      "title": "Transaction activity",
      "description": "This wallet has 128 transactions and shows medium activity."
    },
    {
      "title": "Low risk signal",
      "description": "No obvious suspicious pattern was found in the mock analysis."
    }
  ]
}
```

## Sprint Documentation

- [Sprint 0 Review](docs/sprint-0.md)
- [Sprint 1 Review](docs/sprint-1.md)
- [Sprint 2 Review](docs/sprint-2.md)
- [Sprint 3 Review](docs/sprint-3.md)
