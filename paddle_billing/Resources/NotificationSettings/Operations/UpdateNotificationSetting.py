from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Events import EventTypeName


@dataclass
class UpdateNotificationSetting:
    description:              str                 | Undefined = Undefined()
    destination:              str                 | Undefined = Undefined()
    active:                   bool                | Undefined = Undefined()
    api_version:              int                 | Undefined = Undefined()
    include_sensitive_fields: bool                | Undefined = Undefined()
    subscribed_events:        list[EventTypeName] | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)


