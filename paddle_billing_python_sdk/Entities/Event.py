from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from importlib   import import_module

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Events.EventTypeName import EventTypeName


@dataclass
class Event(Entity):
    event_id:     str
    event_type:  EventTypeName
    occurred_at: datetime
    data:        Entity


    @staticmethod
    def entity_mapping(event_type: str) -> tuple:
        match event_type:
            case 'discount':
                return 'Notifications.NotificationDiscount', 'NotificationDiscount'
            case 'subscription':
                return 'Notifications.NotificationSubscription', 'NotificationSubscription'
            case _:
                return None, str(event_type).title()


    @classmethod
    def from_dict(cls, data: dict) -> Event:
        _type = data['event_type'].split('.')[0] or ''

        event_type_str = data['event_type'].split('.')[0].lower()
        entity_class   = None

        entity_class_path_extra, entity_class_name = Event.entity_mapping(event_type_str)

        entity_class_path = 'paddle_billing_python_sdk.Entities' \
            if entity_class_path_extra is None \
            else f"paddle_billing_python_sdk.Entities.{entity_class_path_extra}"
        print(f"entity_class_path='{entity_class_path}', entity_class_name='{entity_class_name}'")

        try:
            entity_class = getattr(import_module(entity_class_path), entity_class_name)(**data)
        except Exception as error:
            print(f"Error dynamically instantiating an object: {error}")

        if not entity_class:
            raise ValueError(f"Event type '{entity_class_name}' cannot be mapped to an object")
        if not issubclass(entity_class, Entity):
            raise ValueError(f"Event type '{_type}' cannot be mapped to an object")

        return Event(
            data['event_id'],
            EventTypeName(data['event_type']),
            datetime.fromisoformat(data['occurred_at']),
            entity_class.from_dict(data['data']),
        )
