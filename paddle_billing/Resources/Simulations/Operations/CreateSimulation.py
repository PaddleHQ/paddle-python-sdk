from dataclasses import dataclass

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import (
    InvalidArgumentException as InvalidArgumentException,
)
from paddle_billing.Operation import Operation as Operation
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation.SubscriptionCancellationConfigCreate import (
    SimulationConfigCreate as SimulationConfigCreate,
)
from paddle_billing.Undefined import Undefined as Undefined

from paddle_billing.Entities.Events import EventTypeName as EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType as SimulationScenarioType

from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity as SimulationEntity


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
