from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Options import DunningExhaustedAction, PaymentOutcome


@dataclass
class SubscriptionRenewalOptions(Entity, ABC):
    payment_outcome: PaymentOutcome
    dunning_exhausted_action: DunningExhaustedAction | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionRenewalOptions:
        return SubscriptionRenewalOptions(
            payment_outcome=PaymentOutcome(data["payment_outcome"]),
            dunning_exhausted_action=(
                DunningExhaustedAction(data["dunning_exhausted_action"])
                if data.get("dunning_exhausted_action")
                else None
            ),
        )
