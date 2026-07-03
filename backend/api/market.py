from fastapi import APIRouter

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/coins")
def list_coins():
    return {
        "coins": [
            {"symbol": "BTC", "name": "Bitcoin"},
            {"symbol": "ETH", "name": "Ethereum"},
            {"symbol": "SOL", "name": "Solana"},
        ]
    }