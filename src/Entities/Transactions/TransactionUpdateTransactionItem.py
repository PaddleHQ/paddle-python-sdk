from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionUpdateTransactionItem:
    price_id: str
    quantity: int
