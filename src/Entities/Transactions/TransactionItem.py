from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional

from src.Entities.Price import Price

from src.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionItem:
    priceId:   Optional[str]
    price:     Price
    quantity:  int
    proration: Optional[TransactionProration]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionItem:
        return TransactionItem(
            priceId   = data.get('price_id'),
            price     = Price.from_dict(data['price']),
            quantity  = data['quantity'],
            proration = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
        )
