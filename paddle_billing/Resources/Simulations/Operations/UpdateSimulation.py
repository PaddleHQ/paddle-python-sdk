from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType, SimulationStatus

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity


@dataclass
class UpdateSimulation(Operation):
    notification_setting_id: str | Undefined = Undefined()
    type: EventTypeName | SimulationScenarioType | Undefined = Undefined()
    name: str | Undefined = Undefined()
    status: SimulationStatus | Undefined = Undefined()
    payload: NotificationEntity | Undefined = Undefined()
