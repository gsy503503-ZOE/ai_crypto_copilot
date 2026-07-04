import httpx
from fastapi import HTTPException

from backend.core.config import settings


class CoinGeckoClient:
    def __init__(self) -> None:
        self.base_url = settings.coingecko_api_url.rstrip("/")
        self.timeout = settings.coingecko_timeout_seconds

    def _request(self, path: str, params: dict | None = None) -> dict | list:
        url = f"{self.base_url}{path}"
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                raise HTTPException(status_code=404, detail="Coin not found") from exc
            raise HTTPException(
                status_code=502,
                detail="CoinGecko API returned an error",
            ) from exc
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=502,
                detail="Unable to reach CoinGecko API",
            ) from exc

    def get_price(self, coin_id: str, vs_currency: str = "usd") -> dict:
        data = self._request(
            "/simple/price",
            params={
                "ids": coin_id,
                "vs_currencies": vs_currency,
                "include_24hr_change": "true",
                "include_last_updated_at": "true",
            },
        )
        if coin_id not in data:
            raise HTTPException(status_code=404, detail="Coin not found")
        coin = data[coin_id]
        return {
            "coin_id": coin_id,
            "vs_currency": vs_currency,
            "price": coin.get(vs_currency),
            "change_24h": coin.get(f"{vs_currency}_24h_change"),
            "last_updated_at": coin.get("last_updated_at"),
        }

    def get_prices(self, coin_ids: list[str], vs_currency: str = "usd") -> list[dict]:
        if not coin_ids:
            raise HTTPException(status_code=400, detail="At least one coin id is required")

        data = self._request(
            "/simple/price",
            params={
                "ids": ",".join(coin_ids),
                "vs_currencies": vs_currency,
                "include_24hr_change": "true",
                "include_last_updated_at": "true",
            },
        )

        results = []
        for coin_id in coin_ids:
            if coin_id not in data:
                continue
            coin = data[coin_id]
            results.append(
                {
                    "coin_id": coin_id,
                    "vs_currency": vs_currency,
                    "price": coin.get(vs_currency),
                    "change_24h": coin.get(f"{vs_currency}_24h_change"),
                    "last_updated_at": coin.get("last_updated_at"),
                }
            )

        if not results:
            raise HTTPException(status_code=404, detail="No matching coins found")

        return results

    def get_trending(self) -> list[dict]:
        data = self._request("/search/trending")
        coins = data.get("coins", [])
        trending = []
        for item in coins:
            coin = item.get("item", {})
            trending.append(
                {
                    "coin_id": coin.get("id"),
                    "name": coin.get("name"),
                    "symbol": coin.get("symbol"),
                    "market_cap_rank": coin.get("market_cap_rank"),
                    "price_btc": coin.get("price_btc"),
                    "score": coin.get("score"),
                }
            )
        return trending


coingecko_client = CoinGeckoClient()