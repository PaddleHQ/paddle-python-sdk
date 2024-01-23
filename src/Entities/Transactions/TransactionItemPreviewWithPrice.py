from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Price import Price

from src.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionItemPreviewWithPrice:
    price:           Price
    quantity:        int
    includeInTotals: bool
    proration:       TransactionProration | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithPrice:
        return TransactionItemPreviewWithPrice(
            price           = Price.from_dict(data['price']),
            quantity        = data['quantity'],
            includeInTotals = data['include_in_totals'],
            proration       = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
        )
