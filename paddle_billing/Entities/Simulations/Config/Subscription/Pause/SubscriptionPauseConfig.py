from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Pause.SubscriptionPauseEntities import (
    SubscriptionPauseEntities,
)
from paddle_billing.Entities.Simulations.Config.Subscription.Pause.SubscriptionPauseOptions import (
    SubscriptionPauseOptions,
)


@dataclass
class SubscriptionPauseConfig(Entity, ABC):
    entities: SubscriptionPauseEntities
    options: SubscriptionPauseOptions

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionPauseConfig:
        return SubscriptionPauseConfig(
            entities=SubscriptionPauseEntities.from_dict(data["entities"]),
            options=SubscriptionPauseOptions.from_dict(data["options"]),
        )
