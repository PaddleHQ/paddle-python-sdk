from dataclasses import asdict, dataclass

from paddle_billing.Undefined                     import Undefined
from paddle_billing.Entities.Events               import EventTypeName
from paddle_billing.Entities.NotificationSettings import NotificationSettingType


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


