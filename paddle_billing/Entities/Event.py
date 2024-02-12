from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from importlib   import import_module

from paddle_billing.ConditionallyRemoveImportMeta import conditionally_remove_import_meta
from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName


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
                return 'Notifications', 'NotificationDiscount'
            case 'subscription':
                return 'Notifications', 'NotificationSubscription'
            case _:
                return None, str(event_type).title()


    @classmethod
    def from_dict(cls, data: dict) -> Event:
        _type = data['event_type'].split('.')[0] or ''

        event_type_str     = data['event_type'].split('.')[0].lower()
        entity_class       = None
        instantiated_class = None

        entity_module_path, entity_class_name = Event.entity_mapping(event_type_str)

        entity_module_path = 'paddle_billing.Entities' \
            if entity_module_path is None \
            else f"paddle_billing.Entities.{entity_module_path}"

        try:
            imported_module = import_module(f"{entity_module_path}.{entity_class_name}")
            entity_class    = getattr(imported_module, entity_class_name)

            conditionally_remove_import_meta(entity_class, data)
            instantiated_class = entity_class(**data['data'])
        except Exception as error:
            print(f"Error dynamically instantiating a '{entity_module_path}.{entity_class_name}' object: {error}")

        if not entity_class:
            raise ValueError(f"Event type '{entity_class_name}' cannot be mapped to an object")
        if not issubclass(entity_class, Entity):
            raise ValueError(f"Event type '{_type}' cannot be mapped to an object")

        return Event(
            data['event_id'],
            EventTypeName(data['event_type']),
            datetime.fromisoformat(data['occurred_at']),
            instantiated_class.from_dict(data['data']),
        )
