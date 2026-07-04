from pydantic import BaseModel, Field


class CoinPrice(BaseModel):
    coin_id: str
    vs_currency: str
    price: float | None = None
    change_24h: float | None = None
    last_updated_at: int | None = None
    cached: bool = False


class CoinPriceList(BaseModel):
    data: list[CoinPrice]
    cached: bool = False


class TrendingCoin(BaseModel):
    coin_id: str | None = None
    name: str | None = None
    symbol: str | None = None
    market_cap_rank: int | None = None
    price_btc: float | None = None
    score: int | None = None


class TrendingCoinList(BaseModel):
    data: list[TrendingCoin]
    cached: bool = False