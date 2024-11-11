from __future__ import annotations
from dataclasses import dataclass
from paddle_billing.Undefined import Undefined


@dataclass
class TransactionItemPreviewWithPriceId:
    price_id: str
    quantity: int
    include_in_totals: bool | None | Undefined = Undefined()
