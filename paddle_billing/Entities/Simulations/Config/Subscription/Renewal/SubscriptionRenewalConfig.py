from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Renewal.SubscriptionRenewalEntities import (
    SubscriptionRenewalEntities,
)
from paddle_billing.Entities.Simulations.Config.Subscription.Renewal.SubscriptionRenewalOptions import (
    SubscriptionRenewalOptions,
)


@dataclass
class SubscriptionRenewalConfig(Entity):
    entities: SubscriptionRenewalEntities
    options: SubscriptionRenewalOptions

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionRenewalConfig:
        return SubscriptionRenewalConfig(
            entities=SubscriptionRenewalEntities.from_dict(data["entities"]),
            options=SubscriptionRenewalOptions.from_dict(data["options"]),
        )
