from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.deps import get_db
from backend.models.transaction import Transaction
from backend.schemas.transaction import (
    TransactionCategoryUpdate,
    TransactionCreate,
    TransactionNoteUpdate,
    TransactionResponse,
)

from backend.services.transaction_service import normalize_category

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("", response_model=TransactionResponse)
def create_transaction(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    transaction_dict = transaction_data.model_dump()
    transaction_dict["category"] = normalize_category(transaction_dict["category"])

    new_transaction = Transaction(**transaction_dict)

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

@router.get("/summary")
def get_transaction_summary(
    wallet_address: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Transaction)

    if wallet_address:
        query = query.filter(Transaction.wallet_address == wallet_address)

    if category:
        query = query.filter(Transaction.category == category)

    transactions = query.all()

    total_value_usd = 0
    categories = {}

    for transaction in transactions:
        if transaction.value_usd:
            total_value_usd = total_value_usd + transaction.value_usd

        category_name = transaction.category
        if category_name not in categories:
            categories[category_name] = 0

        categories[category_name] = categories[category_name] + 1

    return {
        "wallet_address": wallet_address,
        "category": category,
        "total_transactions": len(transactions),
        "total_value_usd": total_value_usd,
        "categories": categories,
    }

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction

@router.patch("/{transaction_id}/note", response_model=TransactionResponse)
def update_transaction_note(
    transaction_id: int,
    note_data: TransactionNoteUpdate,
    db: Session = Depends(get_db),
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    transaction.note = note_data.note
    db.commit()
    db.refresh(transaction)

    return transaction

@router.patch("/{transaction_id}/category", response_model=TransactionResponse)
def update_transaction_category(
    transaction_id: int,
    category_data: TransactionCategoryUpdate,
    db: Session = Depends(get_db),
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    transaction.category = normalize_category(category_data.category)
    db.commit()
    db.refresh(transaction)

    return transaction

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}