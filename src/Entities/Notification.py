from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity
from src.Entities.Event  import Event

from src.Entities.Events.EventTypeName import EventTypeName

from src.Entities.Notifications.NotificationOrigin import NotificationOrigin
from src.Entities.Notifications.NotificationStatus import NotificationStatus


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
            delivered_at            = datetime.fromisoformat(data['delivered_at']) if 'delivered_at' in data else None,
            replayed_at             = datetime.fromisoformat(data['replayed_at'])  if 'replayed_at'  in data else None,
            origin                  = NotificationOrigin(data['origin']),
            last_attempt_at         = datetime.fromisoformat(data['last_attempt_at']) if 'last_attempt_at' in data else None,
            retry_at                = datetime.fromisoformat(data['retry_at'])        if 'retry_at'        in data else None,
            times_attempted         = data['times_attempted'],
            notification_setting_id = data['notification_setting_id'],
        )
