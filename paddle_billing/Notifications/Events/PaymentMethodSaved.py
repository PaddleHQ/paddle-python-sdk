from datetime import datetime

from paddle_billing.Entities.Event import Event
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.PaymentMethod import PaymentMethod


class PaymentMethodSaved(Event):
    def __init__(
        self,
        event_id: str,
        event_type: EventTypeName,
        occurred_at: datetime,
        data: PaymentMethod,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
