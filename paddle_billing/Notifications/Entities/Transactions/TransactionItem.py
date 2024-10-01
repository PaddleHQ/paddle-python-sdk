from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Price import Price

from paddle_billing.Notifications.Entities.Shared.Proration import Proration


@dataclass
class TransactionItem:
    price_id: str | None
    price: Price
    quantity: int
    proration: Proration | None

    @staticmethod
    def from_dict(data: dict) -> TransactionItem:
        return TransactionItem(
            price_id=data.get("price_id"),
            price=Price.from_dict(data["price"]),
            quantity=data["quantity"],
            proration=Proration.from_dict(data["proration"]) if data.get("proration") else None,
        )
