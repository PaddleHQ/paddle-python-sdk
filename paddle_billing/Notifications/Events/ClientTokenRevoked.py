from datetime import datetime

from paddle_billing.Entities.Event import Event as Event
from paddle_billing.Entities.Events import EventTypeName as EventTypeName

from paddle_billing.Notifications.Entities.ClientToken import ClientToken as ClientToken


class ClientTokenRevoked(Event):
    def __init__(
        self,
        event_id: str,
        event_type: EventTypeName,
        occurred_at: datetime,
        data: ClientToken,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
