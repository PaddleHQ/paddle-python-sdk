from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionItemPreviewWithPriceId:
    price_id:          str
    quantity:          int
    include_in_totals: bool | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithPriceId:
        return TransactionItemPreviewWithPriceId(
            price_id          = data['price_id'],
            quantity          = data['quantity'],
            include_in_totals = data.get('include_in_totals'),
        )
