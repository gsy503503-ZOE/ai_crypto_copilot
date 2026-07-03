from pydantic import BaseModel


class Coin(BaseModel):
    symbol: str
    name: str


class CoinPrice(BaseModel):
    symbol: str
    price_usd: float
    source: str