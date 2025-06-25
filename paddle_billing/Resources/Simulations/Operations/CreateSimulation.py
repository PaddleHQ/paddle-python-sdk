from dataclasses import dataclass

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Operation import Operation
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation.SubscriptionCancellationConfigCreate import (
    SimulationConfigCreate,
)
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType

from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class CreateSimulation(Operation):
    notification_setting_id: str
    type: EventTypeName | SimulationScenarioType
    name: str
    payload: SimulationEntity | None | Undefined = Undefined()
    config: SimulationConfigCreate | None | Undefined = Undefined()

    def __post_init__(self):
        if isinstance(self.config, SimulationConfigCreate) and self.config.get_simulation_type() != self.type:
            raise InvalidArgumentException.incompatible_arguments("config", "type")
