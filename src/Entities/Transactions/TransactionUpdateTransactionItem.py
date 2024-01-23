from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionUpdateTransactionItem:
    priceId:  str
    quantity: int
