from typing import Optional

from pydantic import BaseModel


class Coin(BaseModel):
    symbol: str
    name: str


class CoinPrice(BaseModel):
    symbol: str
    price_usd: float
    change_24h: Optional[float] = None
    last_updated_at: Optional[int] = None
    source: str