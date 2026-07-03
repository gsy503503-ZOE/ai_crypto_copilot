import httpx

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"


def get_simple_price(coin_id: str, vs_currency: str = "usd"):
    url = f"{COINGECKO_BASE_URL}/simple/price"

    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency,
    }

    response = httpx.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()