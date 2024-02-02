from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Entity        import Entity
from paddle_billing.Entities.Event         import Event
from paddle_billing.Entities.Events        import EventTypeName
from paddle_billing.Entities.Notifications import NotificationOrigin, NotificationStatus


@dataclass
class Notification(Entity):
    id:                      str
    type:                    EventTypeName
    status:                  NotificationStatus
    payload:                 Event
    occurred_at:             datetime
    delivered_at:            datetime | None
    replayed_at:             datetime | None
    origin:                  NotificationOrigin
    last_attempt_at:         datetime | None
    retry_at:                datetime | None
    times_attempted:         int
    notification_setting_id: str


    @classmethod
    def from_dict(cls, data: dict) -> Notification:
        return Notification(
            id                      = data['id'],
            type                    = EventTypeName(data['type']),
            status                  = NotificationStatus(data['status']),
            payload                 = Event.from_dict(data['payload']),
            occurred_at             = datetime.fromisoformat(data['occurred_at']),
            origin                  = NotificationOrigin(data['origin']),
            times_attempted         = data['times_attempted'],
            notification_setting_id = data['notification_setting_id'],
            delivered_at            = datetime.fromisoformat(data['delivered_at'])    if data.get('delivered_at')    else None,
            replayed_at             = datetime.fromisoformat(data['replayed_at'])     if data.get('replayed_at')     else None,
            last_attempt_at         = datetime.fromisoformat(data['last_attempt_at']) if data.get('last_attempt_at') else None,
            retry_at                = datetime.fromisoformat(data['retry_at'])        if data.get('retry_at')        else None,
        )
