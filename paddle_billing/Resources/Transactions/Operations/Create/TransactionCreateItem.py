from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TransactionCreateItem:
    price_id: str
    quantity: int
