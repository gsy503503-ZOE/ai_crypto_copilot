from sqlalchemy import Column, DateTime, Float, Integer, String

from backend.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True, nullable=False)
    tx_hash = Column(String, unique=True, index=True, nullable=False)
    chain = Column(String, nullable=False, default="ethereum")
    category = Column(String, nullable=False, default="unknown")
    token_symbol = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    value_usd = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=True)
    note = Column(String, nullable=True)