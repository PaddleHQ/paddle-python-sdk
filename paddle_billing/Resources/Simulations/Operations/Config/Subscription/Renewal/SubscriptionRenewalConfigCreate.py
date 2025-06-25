from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Renewal import (
    SubscriptionRenewalEntitiesCreate,
    SubscriptionRenewalOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.CreateSimulation import SimulationConfigCreate
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionRenewalConfigCreate(SimulationConfigCreate):
    entities: SubscriptionRenewalEntitiesCreate | Undefined = Undefined()
    options: SubscriptionRenewalOptionsCreate | Undefined = Undefined()

    @staticmethod
    def get_simulation_type() -> SimulationScenarioType:
        return SimulationScenarioType.SubscriptionRenewal

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {
            "subscription_renewal": FiltersUndefined.filter_undefined_values(
                {
                    "entities": self.entities,
                    "options": self.options,
                }
            ),
        }
