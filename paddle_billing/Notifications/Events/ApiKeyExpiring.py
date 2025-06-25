from datetime import datetime

from paddle_billing.Entities.Event import Event
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.ApiKey import ApiKey


class ApiKeyExpiring(Event):
    def __init__(
        self,
        event_id: str,
        event_type: EventTypeName,
        occurred_at: datetime,
        data: ApiKey,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
