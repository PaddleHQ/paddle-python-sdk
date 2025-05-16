from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.EventType import EventType
from paddle_billing.Entities.NotificationSettings import NotificationSettingType, NotificationSettingTrafficSource


@dataclass
class NotificationSetting(Entity):
    id: str
    description: str
    type: NotificationSettingType
    destination: str
    active: bool
    api_version: int
    include_sensitive_fields: bool
    subscribed_events: list[EventType]
    endpoint_secret_key: str
    traffic_source: NotificationSettingTrafficSource

    @staticmethod
    def from_dict(data: dict[str, Any]) -> NotificationSetting:
        return NotificationSetting(
            id=data["id"],
            description=data["description"],
            type=NotificationSettingType(data["type"]),
            destination=data["destination"],
            active=data["active"],
            api_version=data["api_version"],
            include_sensitive_fields=data["include_sensitive_fields"],
            subscribed_events=[EventType.from_dict(event) for event in data.get("subscribed_events", [])],
            endpoint_secret_key=data["endpoint_secret_key"],
            traffic_source=NotificationSettingTrafficSource(data["traffic_source"]),
        )
