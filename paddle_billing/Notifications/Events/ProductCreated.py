from datetime import datetime

from paddle_billing.Entities.Event import Event as Event
from paddle_billing.Entities.Events import EventTypeName as EventTypeName

from paddle_billing.Notifications.Entities.Product import Product as Product


class ProductCreated(Event):
    def __init__(
        self,
        event_id: str,
        event_type: EventTypeName,
        occurred_at: datetime,
        data: Product,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
