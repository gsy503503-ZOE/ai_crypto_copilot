from typing import Optional

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    wallet_address: str
    tx_hash: str
    chain: str = "ethereum"
    category: str = "unknown"
    token_symbol: Optional[str] = None
    amount: Optional[float] = None
    value_usd: Optional[float] = None
    timestamp: Optional[str] = None
    note: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    wallet_address: str
    tx_hash: str
    chain: str
    category: str
    token_symbol: Optional[str]
    amount: Optional[float]
    value_usd: Optional[float]
    timestamp: Optional[str]
    note: Optional[str]

    class Config:
        from_attributes = True