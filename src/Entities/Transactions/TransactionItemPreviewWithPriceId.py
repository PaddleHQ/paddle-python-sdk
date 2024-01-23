from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionItemPreviewWithPriceId:
    priceId:         str
    quantity:        int
    includeInTotals: bool | None


    @classmethod
    def from_dict(cls, data: dict) -> TransactionItemPreviewWithPriceId:
        return TransactionItemPreviewWithPriceId(
            priceId         = data['price_id'],
            quantity        = data['quantity'],
            includeInTotals = data.get('include_in_totals'),
        )
