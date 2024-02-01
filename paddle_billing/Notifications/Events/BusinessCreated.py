from datetime import datetime

from paddle_billing.Entities.Business             import Business
from paddle_billing.Entities.Event                import Event
from paddle_billing.Entities.Events.EventTypeName import EventTypeName


class BusinessCreated(Event):
    def __init__(
        self,
        event_id:    str,
        event_type:  EventTypeName,
        occurred_at: datetime,
        data:        Business,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
