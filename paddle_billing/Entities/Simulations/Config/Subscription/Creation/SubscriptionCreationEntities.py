from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Creation.SubscriptionCreationItem import (
    SubscriptionCreationItem,
)


@dataclass
class SubscriptionCreationEntities(Entity, ABC):
    customer_id: str | None
    address_id: str | None
    business_id: str | None
    payment_method_id: str | None
    discount_id: str | None
    transaction_id: str | None
    items: list[SubscriptionCreationItem] | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCreationEntities:
        return SubscriptionCreationEntities(
            customer_id=data.get("customer_id"),
            address_id=data.get("address_id"),
            business_id=data.get("business_id"),
            payment_method_id=data.get("payment_method_id"),
            discount_id=data.get("discount_id"),
            transaction_id=data.get("transaction_id"),
            items=(
                [SubscriptionCreationItem.from_dict(item) for item in data.get("items")] if data.get("items") else None
            ),
        )
