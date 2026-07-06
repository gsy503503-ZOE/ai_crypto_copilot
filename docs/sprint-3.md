# Sprint 3 Review: Wallet Analysis Foundation

## Sprint Goal

Build the first wallet analysis module for AI Crypto Copilot.

By the end of this sprint, the backend can accept a wallet address, validate the address format, and return a mock wallet analysis result.

## Completed Tasks

- Created a wallet API router.
- Added `GET /wallet/ping` to check whether the wallet module is running.
- Added `POST /wallet/analyze` to analyze a wallet address.
- Created wallet request and response schemas.
- Created a wallet service layer.
- Added EVM wallet address validation.
- Added mock wallet data.
- Added wallet risk level calculation.
- Added wallet risk score calculation.
- Added wallet activity level calculation.
- Added generated wallet insights.
- Added an analysis timestamp with `analyzed_at`.
- Added smoke checks for the wallet service.

## API Endpoints

- `GET /wallet/ping`
- `POST /wallet/analyze`

## Example Request

```json
{
  "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
}
```

## Example Response

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

## Problems I Encountered

I learned that a function definition and a function call must match.
I saw a TypeError when calculate_risk_score() expected one argument but received two.
I fixed the bug by updating the function call inside analyze_wallet().
I learned that test scripts can catch this type of mistake quickly.

## What I Learned

A wallet address can be validated with a regular expression.
mock data helps us build and test product logic before connecting to a real blockchain API.
risk_level gives a human-readable risk category.
risk_score gives a numeric risk value.
activity_level describes how active a wallet is.
insights turn raw data into readable analysis.
smoke tests quickly check whether important functions still work.
assert can be used for simple automated checks.
