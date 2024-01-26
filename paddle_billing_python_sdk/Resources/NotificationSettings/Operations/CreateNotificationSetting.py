from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Events.EventTypeName import EventTypeName
from paddle_billing_python_sdk.Entities.NotificationSettings.NotificationSettingType import NotificationSettingType


@dataclass
class CreateNotificationSetting:
    description:              str
    destination:              str
    subscribed_events:        list[EventTypeName]
    type:                     NotificationSettingType
    include_sensitive_fields: bool
    api_version:              int | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)


