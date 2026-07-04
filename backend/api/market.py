from fastapi import APIRouter, HTTPException

from backend.schemas.market import Coin, CoinPrice
from backend.services.market_service import (
    get_market_summary,
    get_real_coin_price,
    get_supported_coins,
)

from typing import List

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/coins", response_model=dict[str, list[Coin]])
def list_coins():
    return {"coins": get_supported_coins()}


@router.get("/coins/{symbol}/price", response_model=CoinPrice)
def get_price(symbol: str):
    coin_price = get_real_coin_price(symbol)

    if coin_price is None:
        raise HTTPException(status_code=404, detail="Coin not found")

    return coin_price

@router.get("/summary", response_model=list[CoinPrice])
def get_summary():
    return get_market_summary()