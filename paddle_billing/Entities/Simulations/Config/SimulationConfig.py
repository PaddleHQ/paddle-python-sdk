from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Subscription.Cancellation import SubscriptionCancellationConfig
from paddle_billing.Entities.Simulations.Config.Subscription.Creation import SubscriptionCreationConfig
from paddle_billing.Entities.Simulations.Config.Subscription.Pause import SubscriptionPauseConfig
from paddle_billing.Entities.Simulations.Config.Subscription.Renewal import SubscriptionRenewalConfig
from paddle_billing.Entities.Simulations.Config.Subscription.Resume import SubscriptionResumeConfig


@dataclass
class SimulationConfig(Entity):
    subscription_creation: SubscriptionCreationConfig | None
    subscription_renewal: SubscriptionRenewalConfig | None
    subscription_pause: SubscriptionPauseConfig | None
    subscription_resume: SubscriptionResumeConfig | None
    subscription_cancellation: SubscriptionCancellationConfig | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SimulationConfig:
        return SimulationConfig(
            subscription_creation=(
                SubscriptionCreationConfig.from_dict(data["subscription_creation"])
                if data.get("subscription_creation")
                else None
            ),
            subscription_renewal=(
                SubscriptionRenewalConfig.from_dict(data["subscription_renewal"])
                if data.get("subscription_renewal")
                else None
            ),
            subscription_pause=(
                SubscriptionPauseConfig.from_dict(data["subscription_pause"])
                if data.get("subscription_pause")
                else None
            ),
            subscription_resume=(
                SubscriptionResumeConfig.from_dict(data["subscription_resume"])
                if data.get("subscription_resume")
                else None
            ),
            subscription_cancellation=(
                SubscriptionCancellationConfig.from_dict(data["subscription_cancellation"])
                if data.get("subscription_cancellation")
                else None
            ),
        )
