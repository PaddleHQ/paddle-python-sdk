from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Events import EventTypeName as EventTypeName
from paddle_billing.Entities.NotificationSettings import (
    NotificationSettingType as NotificationSettingType,
    NotificationSettingTrafficSource as NotificationSettingTrafficSource,
)


@dataclass
class CreateNotificationSetting(Operation):
    description: str
    destination: str
    subscribed_events: list[EventTypeName]
    type: NotificationSettingType
    include_sensitive_fields: bool
    api_version: int | Undefined = Undefined()
    traffic_source: NotificationSettingTrafficSource | Undefined = Undefined()
