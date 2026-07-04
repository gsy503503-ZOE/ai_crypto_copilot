from fastapi import APIRouter, Query

from backend.cache import cache
from backend.core.config import settings
from backend.schemas.market import CoinPrice, CoinPriceList, TrendingCoin, TrendingCoinList
from backend.services.coingecko import coingecko_client

router = APIRouter(prefix="/v1/market", tags=["market"])


@router.get("/price/{coin_id}", response_model=CoinPrice)
def get_coin_price(coin_id: str, vs_currency: str = Query(default="usd", min_length=3, max_length=10)):
    cache_key = f"market:price:{coin_id}:{vs_currency.lower()}"
    cached_value = cache.get(cache_key)
    if cached_value is not None:
        return CoinPrice(**cached_value, cached=True)

    payload = coingecko_client.get_price(coin_id=coin_id, vs_currency=vs_currency.lower())
    cache.set(cache_key, payload, settings.cache_ttl_seconds)
    return CoinPrice(**payload, cached=False)


@router.get("/prices", response_model=CoinPriceList)
def get_coin_prices(
    ids: str = Query(..., description="Comma-separated CoinGecko coin ids"),
    vs_currency: str = Query(default="usd", min_length=3, max_length=10),
):
    coin_ids = [coin_id.strip().lower() for coin_id in ids.split(",") if coin_id.strip()]
    cache_key = f"market:prices:{','.join(sorted(coin_ids))}:{vs_currency.lower()}"
    cached_value = cache.get(cache_key)
    if cached_value is not None:
        return CoinPriceList(
            data=[CoinPrice(**item, cached=True) for item in cached_value],
            cached=True,
        )

    payload = coingecko_client.get_prices(coin_ids=coin_ids, vs_currency=vs_currency.lower())
    cache.set(cache_key, payload, settings.cache_ttl_seconds)
    return CoinPriceList(
        data=[CoinPrice(**item, cached=False) for item in payload],
        cached=False,
    )


@router.get("/trending", response_model=TrendingCoinList)
def get_trending_coins():
    cache_key = "market:trending"
    cached_value = cache.get(cache_key)
    if cached_value is not None:
        return TrendingCoinList(
            data=[TrendingCoin(**item) for item in cached_value],
            cached=True,
        )

    payload = coingecko_client.get_trending()
    cache.set(cache_key, payload, settings.cache_ttl_seconds)
    return TrendingCoinList(
        data=[TrendingCoin(**item) for item in payload],
        cached=False,
    )