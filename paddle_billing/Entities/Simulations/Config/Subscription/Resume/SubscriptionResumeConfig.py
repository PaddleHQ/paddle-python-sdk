from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Resume.SubscriptionResumeEntities import (
    SubscriptionResumeEntities,
)
from paddle_billing.Entities.Simulations.Config.Subscription.Resume.SubscriptionResumeOptions import (
    SubscriptionResumeOptions,
)


@dataclass
class SubscriptionResumeConfig(Entity, ABC):
    entities: SubscriptionResumeEntities
    options: SubscriptionResumeOptions

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionResumeConfig:
        return SubscriptionResumeConfig(
            entities=SubscriptionResumeEntities.from_dict(data["entities"]),
            options=SubscriptionResumeOptions.from_dict(data["options"]),
        )
