from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    wallet_address: str
    tx_hash: str
    chain: str = "ethereum"
    category: str = "unknown"
    token_symbol: Optional[str] = None
    amount: Optional[float] = None
    value_usd: Optional[float] = None
    timestamp: Optional[datetime] = None
    note: Optional[str] = None
    labels: List[str] = Field(default_factory=list)


class TransactionNoteUpdate(BaseModel):
    note: str


class TransactionCategoryUpdate(BaseModel):
    category: str


class TransactionLabelsUpdate(BaseModel):
    labels: List[str]


class TransactionResponse(BaseModel):
    id: int
    wallet_address: str
    tx_hash: str
    chain: str
    category: str
    token_symbol: Optional[str]
    amount: Optional[float]
    value_usd: Optional[float]
    timestamp: Optional[datetime]
    note: Optional[str]
    labels: List[str]

    class Config:
        from_attributes = True
