from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Cancellation.SubscriptionCancellationEntities import (
    SubscriptionCancellationEntities,
)
from paddle_billing.Entities.Simulations.Config.Subscription.Cancellation.SubscriptionCancellationOptions import (
    SubscriptionCancellationOptions,
)


@dataclass
class SubscriptionCancellationConfig(Entity, ABC):
    entities: SubscriptionCancellationEntities
    options: SubscriptionCancellationOptions

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCancellationConfig:
        return SubscriptionCancellationConfig(
            entities=SubscriptionCancellationEntities.from_dict(data["entities"]),
            options=SubscriptionCancellationOptions.from_dict(data["options"]),
        )
