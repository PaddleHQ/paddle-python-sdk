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
    id:                    str
    type:                  EventTypeName
    status:                NotificationStatus
    payload:               Event
    occurredAt:            datetime
    deliveredAt:           datetime | None
    replayedAt:            datetime | None
    origin:                NotificationOrigin
    lastAttemptAt:         datetime | None
    retryAt:               datetime | None
    timesAttempted:        int
    notificationSettingId: str


    @classmethod
    def from_dict(cls, data: dict) -> Notification:
        return Notification(
            id                    = data['id'],
            type                  = EventTypeName(data['type']),
            status                = NotificationStatus(data['status']),
            payload               = Event.from_dict(data['payload']),
            occurredAt            = datetime.fromisoformat(data['occurred_at']),
            deliveredAt           = datetime.fromisoformat(data['delivered_at']) if 'delivered_at' in data else None,
            replayedAt            = datetime.fromisoformat(data['replayed_at'])  if 'replayed_at'  in data else None,
            origin                = NotificationOrigin(data['origin']),
            lastAttemptAt         = datetime.fromisoformat(data['last_attempt_at']) if 'last_attempt_at' in data else None,
            retryAt               = datetime.fromisoformat(data['retry_at'])        if 'retry_at'        in data else None,
            timesAttempted        = data['times_attempted'],
            notificationSettingId = data['notification_setting_id']
        )
