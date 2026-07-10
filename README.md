# AI Crypto Ledger Copilot

AI Crypto Ledger Copilot is a backend project for organizing, analyzing, and explaining crypto wallet activity.

This project started as AI Crypto Copilot, a broader crypto research assistant. After several sprints, the product direction became clearer: the core use case is a crypto transaction ledger copilot that helps users understand wallet activity, transaction records, labels, and summary metrics.

## Goal

Build a practical backend system that helps users collect, label, filter, summarize, and eventually explain crypto wallet transactions.

The long-term goal is to build an AI-assisted ledger product for crypto users, builders, analysts, and remote backend engineering portfolio review.

## Current Status

Current release: `v0.5.0`

Current development: `Sprint 5 - Transaction Labeling completed`

Sprint 4 adds the transaction ledger foundation. The backend can now create, list, filter, update, delete, and summarize wallet transaction records.

Sprint 5 adds transaction labeling. The backend can now save labels on transactions, validate labels, update labels, filter transactions by label, summarize label distribution, and suggest labels from transaction data.

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
- Transaction ledger model
- Transaction creation and listing
- Transaction filtering by wallet address and category
- Transaction detail lookup by id
- Transaction note and category updates
- Transaction deletion
- Transaction category validation and normalization
- Transaction summary metrics
- Transaction labels
- Transaction label validation and normalization
- Transaction label update endpoint
- Transaction label filtering
- Transaction label summary metrics
- Transaction label options endpoint
- Rule-based transaction label suggestions
- Sprint documentation and GitHub releases

## Product Direction

The project is moving from a general crypto copilot toward a transaction ledger copilot.

Instead of focusing on trading advice, the product focuses on a lower-risk and more engineering-oriented problem:

- What happened in this wallet?
- How should these transactions be organized?
- Which transactions belong to transfers, swaps, fees, airdrops, staking rewards, or bridges?
- What is the total wallet activity?
- What are the useful summary metrics?
- How can AI later explain transaction history in plain English?

This direction better matches backend engineering roles that require API design, database modeling, authentication, data processing, testing, and production readiness.

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
- Frontend dashboard

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
- v0.3.0 Wallet analysis - completed
- v0.4.0 Transaction ledger - completed
- v0.5.0 Transaction labeling - completed
- v0.6.0 Tests and logging - planned
- v0.7.0 Background sync - planned
- v0.8.0 Docker and PostgreSQL - planned
- v0.9.0 AI transaction explanation - planned
- v1.0.0 Frontend dashboard - planned

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

### Transaction Ledger

- Transaction creation
- Transaction listing
- Transaction lookup by id
- Transaction deletion
- Transaction note update
- Transaction category update
- Wallet address filtering
- Category filtering
- Category validation
- Category normalization
- Transaction summary metrics
- Empty state response for filtered summary results

### Transaction Labeling

- Manual transaction labels
- Allowed label validation
- Label normalization
- Duplicate label removal
- Label suggestions based on category, token, and USD value
- Label option endpoint
- Transaction list filtering by label
- Transaction summary filtering by label
- Label distribution in summary metrics

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

### Transactions

- `POST /transactions`
- `GET /transactions`
- `GET /transactions/summary`
- `GET /transactions/labels/options`
- `GET /transactions/{transaction_id}`
- `PATCH /transactions/{transaction_id}/note`
- `PATCH /transactions/{transaction_id}/category`
- `PATCH /transactions/{transaction_id}/labels`
- `GET /transactions/{transaction_id}/labels/suggestions`
- `DELETE /transactions/{transaction_id}`

## Example Transaction Request

```json
{
  "wallet_address": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
  "tx_hash": "0xtesttxhash0003",
  "chain": "ethereum",
  "category": "swap",
  "token_symbol": "USDC",
  "amount": 100,
  "value_usd": 100,
  "timestamp": "2026-07-09T10:00:00",
  "note": "Test transaction",
  "labels": ["defi", "stablecoin"]
}
```

## Example Transaction Summary Response

```json
{
  "message": "Transaction summary generated successfully",
  "wallet_address": null,
  "category": null,
  "label": null,
  "total_transactions": 2,
  "total_amount": 350.75,
  "total_value_usd": 350.75,
  "average_value_usd": 175.38,
  "largest_transaction_value_usd": 250.75,
  "categories": {
    "swap": 2
  },
  "labels": {
    "defi": 2,
    "stablecoin": 1
  }
}
```

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
- [Sprint 4 Review](docs/sprint-4.md)
- [Sprint 5 Review](docs/sprint-5.md)
