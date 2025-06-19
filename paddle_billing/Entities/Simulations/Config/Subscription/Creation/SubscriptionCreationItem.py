from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class SubscriptionCreationItem(Entity, ABC):
    price_id: str
    quantity: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCreationItem:
        return SubscriptionCreationItem(
            price_id=data["price_id"],
            quantity=data["quantity"],
        )
