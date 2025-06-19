from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Options import EffectiveFrom


@dataclass
class SubscriptionPauseOptions(Entity, ABC):
    effective_from: EffectiveFrom
    has_past_due_transaction: bool

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionPauseOptions:
        return SubscriptionPauseOptions(
            effective_from=EffectiveFrom(data["effective_from"]),
            has_past_due_transaction=data["has_past_due_transaction"],
        )
