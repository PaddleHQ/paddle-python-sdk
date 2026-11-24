from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.FiltersUndefined import FiltersUndefined as FiltersUndefined
from paddle_billing.Entities.Simulation import SimulationScenarioType as SimulationScenarioType
from paddle_billing.Resources.Simulations.Operations.Config.SimulationConfigCreate import (
    SimulationConfigCreate as SimulationConfigCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Resume.SubscriptionResumeEntitiesCreate import (
    SubscriptionResumeEntitiesCreate as SubscriptionResumeEntitiesCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Resume.SubscriptionResumeOptionsCreate import (
    SubscriptionResumeOptionsCreate as SubscriptionResumeOptionsCreate,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class SubscriptionResumeConfigCreate(SimulationConfigCreate):
    entities: SubscriptionResumeEntitiesCreate | Undefined = Undefined()
    options: SubscriptionResumeOptionsCreate | Undefined = Undefined()

    @staticmethod
    def get_simulation_type() -> SimulationScenarioType:
        return SimulationScenarioType.SubscriptionResume

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {
            "subscription_resume": FiltersUndefined.filter_undefined_values(
                {
                    "entities": self.entities,
                    "options": self.options,
                }
            ),
        }
