from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class SubscriptionRenewalEntities(Entity):
    subscription_id: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionRenewalEntities:
        return SubscriptionRenewalEntities(
            subscription_id=data.get("subscription_id"),
        )
