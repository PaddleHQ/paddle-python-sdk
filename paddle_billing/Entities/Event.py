from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from importlib   import import_module

from paddle_billing.ConditionallyRemoveImportMeta import conditionally_remove_import_meta

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity


@dataclass
class Event(Entity):
    event_id:     str
    event_type:  EventTypeName
    occurred_at: datetime
    data:        NotificationEntity


    @classmethod
    def from_dict(cls, data: dict) -> Event:
        _type = data['event_type'].split('.')[0] or ''

        entity_class_name  = data['event_type'].split('.')[0].lower().title()
        entity_class       = None
        instantiated_class = None
        entity_module_path = 'paddle_billing.Notifications.Entities'

        try:
            imported_module = import_module(f"{entity_module_path}.{entity_class_name}")
            entity_class    = getattr(imported_module, entity_class_name)

            conditionally_remove_import_meta(entity_class, data)
            instantiated_class = entity_class  # (**data['data'])
        except Exception as error:
            print(f"Error dynamically instantiating a '{entity_module_path}.{entity_class_name}' object: {error}")

        if not entity_class:
            raise ValueError(f"Event type '{entity_class_name}' cannot be mapped to an object")
        if not issubclass(entity_class, NotificationEntity):
            raise ValueError(f"Event type '{_type}' is not of NotificationEntity")

        return Event(
            data['event_id'],
            EventTypeName(data['event_type']),
            datetime.fromisoformat(data['occurred_at']),
            instantiated_class.from_dict(data['data']),
        )
