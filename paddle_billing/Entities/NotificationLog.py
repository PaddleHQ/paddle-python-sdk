from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Entity import Entity


@dataclass
class NotificationLog(Entity):
    id:                    str
    response_code:         int
    response_content_type: str | None
    response_body:         str
    attempted_at:          datetime


    @classmethod
    def from_dict(cls, data: dict) -> NotificationLog:
        return NotificationLog(
            id                    = data['id'],
            response_code         = data['response_code'],
            response_content_type = data.get('response_content_type'),
            response_body         = data['response_body'],
            attempted_at          = datetime.fromisoformat(data['attempted_at']),
        )
