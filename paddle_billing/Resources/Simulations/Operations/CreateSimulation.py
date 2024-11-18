from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity


@dataclass
class CreateSimulation(Operation):
    notification_setting_id: str
    type: EventTypeName | SimulationScenarioType
    name: str
    payload: NotificationEntity | None | Undefined = Undefined()
