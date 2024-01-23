from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Price import Price

from src.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionItem:
    priceId:   str | None
    price:     Price
    quantity:  int
    proration: TransactionProration | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItem:
        return TransactionItem(
            priceId   = data.get('price_id'),
            price     = Price.from_dict(data['price']),
            quantity  = data['quantity'],
            proration = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
        )
