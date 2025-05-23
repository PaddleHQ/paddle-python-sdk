from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Price import Price

from paddle_billing.Entities.Shared.Proration import Proration


@dataclass
class TransactionItem:
    price: Price
    quantity: int
    proration: Proration | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionItem:
        return TransactionItem(
            price=Price.from_dict(data["price"]),
            quantity=data["quantity"],
            proration=Proration.from_dict(data["proration"]) if data.get("proration") else None,
        )
