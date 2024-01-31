from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionCreateItem:
    price_id: str
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> TransactionCreateItem:
        return TransactionCreateItem(
            price_id = data['price_id'],
            quantity = data['quantity'],
        )
