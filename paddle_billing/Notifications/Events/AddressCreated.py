from datetime import datetime

from paddle_billing.Entities.Event import Event
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.Address import Address


class AddressCreated(Event):
    def __init__(
        self,
        event_id: str,
        event_type: EventTypeName,
        occurred_at: datetime,
        data: Address,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
