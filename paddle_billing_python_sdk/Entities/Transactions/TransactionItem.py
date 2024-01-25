from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Price import Price

from paddle_billing_python_sdk.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionItem:
    price_id:  str | None
    price:     Price
    quantity:  int
    proration: TransactionProration | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItem:
        return TransactionItem(
            price_id  = data.get('price_id'),
            price     = Price.from_dict(data['price']),
            quantity  = data['quantity'],
            proration = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
        )
