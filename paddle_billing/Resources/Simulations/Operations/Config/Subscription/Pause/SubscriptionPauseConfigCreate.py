from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined as FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType as SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Pause.SubscriptionPauseEntitiesCreate import (
    SubscriptionPauseEntitiesCreate as SubscriptionPauseEntitiesCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Pause.SubscriptionPauseOptionsCreate import (
    SubscriptionPauseOptionsCreate as SubscriptionPauseOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.CreateSimulation import (
    SimulationConfigCreate as SimulationConfigCreate,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class SubscriptionPauseConfigCreate(SimulationConfigCreate):
    entities: SubscriptionPauseEntitiesCreate | Undefined = Undefined()
    options: SubscriptionPauseOptionsCreate | Undefined = Undefined()

    @staticmethod
    def get_simulation_type() -> SimulationScenarioType:
        return SimulationScenarioType.SubscriptionPause

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {
            "subscription_pause": FiltersUndefined.filter_undefined_values(
                {
                    "entities": self.entities,
                    "options": self.options,
                }
            ),
        }
