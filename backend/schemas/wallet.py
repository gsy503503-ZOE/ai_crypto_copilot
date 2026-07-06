from typing import List

from pydantic import BaseModel


class WalletAnalyzeRequest(BaseModel):
    address: str


class WalletInsight(BaseModel):
    title: str
    description: str


class WalletAnalyzeResponse(BaseModel):
    address: str
    risk_level: str
    risk_score: int
    activity_level: str
    total_transactions: int
    analyzed_at: str
    insights: List[WalletInsight]