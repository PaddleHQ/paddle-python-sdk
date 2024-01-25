from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from importlib   import import_module

from src import log

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Events.EventTypeName import EventTypeName


@dataclass
class Event(Entity):
    eventId:    str
    eventType:  EventTypeName
    occurredAt: datetime
    data:       Entity


    @staticmethod
    def entity_mapping(event_type: str) -> str:
        match event_type:
            case 'discount':
                return 'NotificationDiscount'
            case 'subscription':
                return 'NotificationSubscription'
            case _:
                return str(event_type).title()


    @classmethod
    def from_dict(cls, data: dict):
        _type = data['event_type'].split('.')[0] or ''

        event_type_str    = data['event_type'].split('.')[0].lower()
        entity_class_name = Event.entity_mapping(event_type_str)
        entity_class      = None

        try:  # TODO this is probably broken
            entity_class = getattr(import_module('src.Entities'), entity_class_name)()
            log.debug(f"entity_class={entity_class}")
        except Exception as error:
            log.error(f"Error dynamically instantiating an object: {error}")

        if not entity_class:
            raise ValueError(f"Event type '{event_type_str}' cannot be mapped to an object")
        if not issubclass(entity_class, Entity):
            raise ValueError(f"Event type '{_type}' cannot be mapped to an object")

        return cls(
            data['event_id'],
            EventTypeName(data['event_type']),  # Assuming EventTypeName has a similar factory method
            datetime.fromisoformat(data['occurred_at']),
            entity_class.from_dict(data['data']),  # Assuming each entity class has a similar factory method
        )
