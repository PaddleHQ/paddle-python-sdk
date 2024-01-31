from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Price import Price

from paddle_billing.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionItemPreviewWithPrice:
    price:             Price
    quantity:          int
    include_in_totals: bool
    proration:         TransactionProration | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithPrice:
        return TransactionItemPreviewWithPrice(
            price             = Price.from_dict(data['price']),
            quantity          = data['quantity'],
            include_in_totals = data['include_in_totals'],
            proration         = TransactionProration.from_dict(data['proration']) if data.get('proration') else None,
        )
