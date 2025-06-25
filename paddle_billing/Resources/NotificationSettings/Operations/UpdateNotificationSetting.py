from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.NotificationSettings import NotificationSettingTrafficSource


@dataclass
class UpdateNotificationSetting(Operation):
    description: str | Undefined = Undefined()
    destination: str | Undefined = Undefined()
    active: bool | Undefined = Undefined()
    api_version: int | Undefined = Undefined()
    include_sensitive_fields: bool | Undefined = Undefined()
    subscribed_events: list[EventTypeName] | Undefined = Undefined()
    traffic_source: NotificationSettingTrafficSource | Undefined = Undefined()
