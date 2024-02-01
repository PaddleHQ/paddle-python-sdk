from datetime import datetime

from paddle_billing.Entities.Event                                  import Event
from paddle_billing.Entities.Events.EventTypeName                   import EventTypeName
from paddle_billing.Entities.Notifications.NotificationSubscription import NotificationSubscription


class SubscriptionImported(Event):
    def __init__(
        self,
        event_id:    str,
        event_type:  EventTypeName,
        occurred_at: datetime,
        data:        NotificationSubscription,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
