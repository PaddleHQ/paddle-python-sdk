from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity


@dataclass
class NotificationLog(Entity):
    id:                  str
    responseCode:        int
    responseContentType: str | None
    responseBody:        str
    attempted_at:        datetime


    @classmethod
    def from_dict(cls, data: dict) -> NotificationLog:
        return NotificationLog(
            id                  = data['id'],
            responseCode        = data['response_code'],
            responseContentType = data.get('response_content_type'),
            responseBody        = data['response_body'],
            attempted_at        = datetime.fromisoformat(data['attempted_at']),
        )
