from fastapi import APIRouter, HTTPException
from backend.services.market_service import get_coin_price, get_supported_coins

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/coins")
def list_coins():
    return {"coins": get_supported_coins()}

@router.get("/coins/{symbol}/price")
def get_price(symbol: str):
    coin_price = get_coin_price(symbol)

    if coin_price is None:
        raise HTTPException(status_code=404, detail="Coin not found")

    return coin_price