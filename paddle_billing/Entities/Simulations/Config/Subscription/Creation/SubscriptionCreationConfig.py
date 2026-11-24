from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity as Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Creation.SubscriptionCreationEntities import (
    SubscriptionCreationEntities as SubscriptionCreationEntities,
)
from paddle_billing.Entities.Simulations.Config.Subscription.Creation.SubscriptionCreationOptions import (
    SubscriptionCreationOptions as SubscriptionCreationOptions,
)


@dataclass
class SubscriptionCreationConfig(Entity):
    entities: SubscriptionCreationEntities
    options: SubscriptionCreationOptions

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCreationConfig:
        return SubscriptionCreationConfig(
            entities=SubscriptionCreationEntities.from_dict(data["entities"]),
            options=SubscriptionCreationOptions.from_dict(data["options"]),
        )
