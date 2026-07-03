from backend.services.coingecko_client import get_simple_price

def get_real_coin_price(symbol: str):
    symbol_to_id = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "SOL": "solana",
    }

    symbol_upper = symbol.upper()
    coin_id = symbol_to_id.get(symbol_upper)

    if coin_id is None:
        return None

    try:
        data = get_simple_price(coin_id)

        return {
            "symbol": symbol_upper,
            "price_usd": data[coin_id]["usd"],
            "change_24h": data[coin_id]["usd_24h_change"],
            "last_updated_at": data[coin_id]["last_updated_at"],
            "source": "coingecko",
        }
    except Exception:
        return get_coin_price(symbol_upper)

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

    if data is None:
        return None
    
    return {
        "symbol": data["symbol"],
        "price_usd": data["price_usd"],
        "change_24h": None,
        "last_updated_at": None,
        "source": "mock",
    }