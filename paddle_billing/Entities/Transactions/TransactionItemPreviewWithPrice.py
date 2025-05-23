from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Transactions.TransactionPreviewPrice import TransactionPreviewPrice

from paddle_billing.Entities.Shared.Proration import Proration


@dataclass
class TransactionItemPreviewWithPrice:
    price: TransactionPreviewPrice
    quantity: int
    include_in_totals: bool
    proration: Proration | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionItemPreviewWithPrice:
        return TransactionItemPreviewWithPrice(
            price=TransactionPreviewPrice.from_dict(data["price"]),
            quantity=data["quantity"],
            include_in_totals=data["include_in_totals"],
            proration=Proration.from_dict(data["proration"]) if data.get("proration") else None,
        )
