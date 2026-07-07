from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api.deps import get_db
from backend.models.transaction import Transaction
from backend.schemas.transaction import TransactionCreate, TransactionResponse

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("", response_model=TransactionResponse)
def create_transaction(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = Transaction(**transaction_data.model_dump())

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


@router.get("", response_model=List[TransactionResponse])
def list_transactions(
    wallet_address: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Transaction)

    if wallet_address:
        query = query.filter(Transaction.wallet_address == wallet_address)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()