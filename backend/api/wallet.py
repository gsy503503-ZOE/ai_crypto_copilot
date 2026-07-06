from fastapi import APIRouter, HTTPException

from backend.schemas.wallet import WalletAnalyzeRequest, WalletAnalyzeResponse
from backend.services.wallet_service import analyze_wallet, is_valid_evm_address

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("/ping")
def wallet_ping():
    return {"message": "Wallet API is running"}

@router.post("/analyze", response_model=WalletAnalyzeResponse)
def analyze_wallet_endpoint(request: WalletAnalyzeRequest):
    if not is_valid_evm_address(request.address):
        raise HTTPException(status_code=400, detail="Invalid wallet address")

    return analyze_wallet(request.address)