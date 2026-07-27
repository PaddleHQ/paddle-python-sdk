from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Price import Price


@dataclass
class SubscriptionHistoryDetailItem:
    price: Price
    quantity: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailItem:
        return SubscriptionHistoryDetailItem(
            price=Price.from_dict(data["price"]),
            quantity=data["quantity"],
        )
