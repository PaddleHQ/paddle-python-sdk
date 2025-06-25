from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config import SimulationConfigCreate
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation import (
    SubscriptionCancellationEntitiesCreate,
    SubscriptionCancellationOptionsCreate,
)
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionCancellationConfigCreate(SimulationConfigCreate):
    entities: SubscriptionCancellationEntitiesCreate | Undefined = Undefined()
    options: SubscriptionCancellationOptionsCreate | Undefined = Undefined()

    @staticmethod
    def get_simulation_type() -> SimulationScenarioType:
        return SimulationScenarioType.SubscriptionCancellation

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {
            "subscription_cancellation": FiltersUndefined.filter_undefined_values(
                {
                    "entities": self.entities,
                    "options": self.options,
                }
            ),
        }
