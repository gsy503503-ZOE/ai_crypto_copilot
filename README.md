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

Sprint 0 is in progress.

Completed:

- Initialized GitHub repository
- Created FastAPI backend entrypoint
- Added health check endpoint
- Organized backend API routes
- Added FastAPI project metadata

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

- v0.0.1 Backend foundation
- v0.1 User authentication
- v0.2 Crypto market data
- v0.3 Wallet analysis
- v0.4 AI research assistant
