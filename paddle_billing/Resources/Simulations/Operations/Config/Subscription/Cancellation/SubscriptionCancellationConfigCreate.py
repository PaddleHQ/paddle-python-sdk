from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined as FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType as SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config.SimulationConfigCreate import (
    SimulationConfigCreate as SimulationConfigCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation.SubscriptionCancellationEntitiesCreate import (
    SubscriptionCancellationEntitiesCreate as SubscriptionCancellationEntitiesCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation.SubscriptionCancellationOptionsCreate import (
    SubscriptionCancellationOptionsCreate as SubscriptionCancellationOptionsCreate,
)
from paddle_billing.Undefined import Undefined as Undefined


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
