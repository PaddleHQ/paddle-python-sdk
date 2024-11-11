from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TransactionUpdateItem:
    price_id: str
    quantity: int
