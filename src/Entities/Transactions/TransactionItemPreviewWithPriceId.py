from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionItemPreviewWithPriceId:
    priceId:         str
    quantity:        int
    includeInTotals: bool | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithPriceId:
        return TransactionItemPreviewWithPriceId(
            priceId         = data['price_id'],
            quantity        = data['quantity'],
            includeInTotals = data.get('include_in_totals'),
        )
