def get_supported_coins():
    return [
        {"symbol": "BTC", "name": "Bitcoin"},
        {"symbol": "ETH", "name": "Ethereum"},
        {"symbol": "SOL", "name": "Solana"},
    ]

def get_coin_price(symbol: str):
    prices = {
        "BTC": {"symbol": "BTC", "price_usd": 65000},
        "ETH": {"symbol": "ETH", "price_usd": 3500},
        "SOL": {"symbol": "SOL", "price_usd": 150},
    }

    return prices.get(symbol.upper())