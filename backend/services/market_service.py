MOCK_MARKET_DATA = {
    "BTC": {"symbol": "BTC", "name": "Bitcoin", "price_usd": 65000.0},
    "ETH": {"symbol": "ETH", "name": "Ethereum", "price_usd": 3500.0},
    "SOL": {"symbol": "SOL", "name": "Solana", "price_usd": 150.0},
}


def get_supported_coins():
    return [
        {
            "symbol": coin["symbol"],
            "name": coin["name"],
        }
        for coin in MOCK_MARKET_DATA.values()
    ]


def get_coin_price(symbol: str):
    return MOCK_MARKET_DATA.get(symbol.upper())