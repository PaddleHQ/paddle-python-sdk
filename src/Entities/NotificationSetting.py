from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Collections.EventTypeCollection import EventTypeCollection

from src.Entities.NotificationSettings.NotificationSettingType import NotificationSettingType


@dataclass
class NotificationSetting(Entity):
    id:                     str
    description:            str
    type:                   NotificationSettingType
    destination:            str
    active:                 bool
    apiVersion:             int
    includeSensitiveFields: bool
    subscribedEvents:       EventTypeCollection
    endpointSecretKey:      str


    @classmethod
    def from_dict(cls, data: dict) -> NotificationSetting:
        return NotificationSetting(
            id                     = data['id'],
            description            = data['description'],
            type                   = NotificationSettingType(data['type']),
            destination            = data['destination'],
            active                 = data['active'],
            apiVersion             = data['api_version'],
            includeSensitiveFields = data['include_sensitive_fields'],
            subscribedEvents       = EventTypeCollection.from_dict(data['subscribed_events']),
            endpointSecretKey      = data['endpoint_secret_key'],
        )
