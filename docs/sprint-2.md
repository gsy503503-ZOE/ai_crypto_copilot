# Sprint 2 Review: Crypto Market Data

## Sprint Goal

Add crypto market data features to AI Crypto Colipot.
By the end of Sprint 2, the backend should be able to fetch and return basic cryptocurrency market data.

## Completed Tasks

### 1. Market Coins Endpoint

I added the first market data endpoint:
- 'GET /market/coins'
This endpoint returns a list of support crypto coins.
For now, it uses mock data for BTC, ETH, and SQL.
The goal of this step was to create the market API structure before connecting to real external market data API.

## 2. Mock Coin Price Endpoint

I added a mock coin price endpoint:
- 'GET /market/coins/{symbol}/price'
This endpoint returns mock USD prices for supported coins.
It supports lowercase and uppercase symbols, so both 'BTC' and 'btc' work.
If the coin is not supported, the backend returns a '404 Coin not found' response.
 