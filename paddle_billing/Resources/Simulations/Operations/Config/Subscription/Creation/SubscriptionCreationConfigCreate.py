from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined as FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType as SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Creation.SubscriptionCreationEntitiesCreate import (
    SubscriptionCreationEntitiesCreate as SubscriptionCreationEntitiesCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Creation.SubscriptionCreationOptionsCreate import (
    SubscriptionCreationOptionsCreate as SubscriptionCreationOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.CreateSimulation import (
    SimulationConfigCreate as SimulationConfigCreate,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class SubscriptionCreationConfigCreate(SimulationConfigCreate):
    entities: SubscriptionCreationEntitiesCreate | Undefined = Undefined()
    options: SubscriptionCreationOptionsCreate | Undefined = Undefined()

    @staticmethod
    def get_simulation_type() -> SimulationScenarioType:
        return SimulationScenarioType.SubscriptionCreation

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {
            "subscription_creation": FiltersUndefined.filter_undefined_values(
                {
                    "entities": self.entities,
                    "options": self.options,
                }
            ),
        }
