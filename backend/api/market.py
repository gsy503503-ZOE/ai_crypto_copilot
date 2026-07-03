from fastapi import APIRouter

from backend.services.market_service import get_supported_coins

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/coins")
def list_coins():
    return {"coins": get_supported_coins()}