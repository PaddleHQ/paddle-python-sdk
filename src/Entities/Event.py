from src.Entities.Entity                import Adjustment, Entity
from src.Entities.Event.EventTypeName   import EventTypeName
from src.Entities.Notification          import NotificationDiscount, NotificationSubscription
from datetime                           import datetime
from abc                                import ABC, abstractmethod


class Event(Entity):  # Assuming Entity is already defined as an ABC
    def __init__(self, event_id: str, event_type: EventTypeName, occurred_at: datetime, data: 'Entity'):
        self.event_id = event_id
        self.event_type = event_type
        self.occurred_at = occurred_at
        self.data = data


    @classmethod
    def make(cls, data: dict):
        type_ = data['event_type'].split('.')[0] or ''

        def entity_mapping(event_type):
            match event_type:
                case "discount":
                    return NotificationDiscount
                case "subscription":
                    return NotificationSubscription
                case _:
                    return str(event_type).title()

        entity_mapping  = entity_mapping(type)
        entity          = None  # TODO do import module stuff here

        if not issubclass(entity, Entity):
            raise ValueError(f"Event type '{type_}' cannot be mapped to an object")

        return cls(
            data['event_id'],
            EventTypeName.make(data['event_type']),  # Assuming EventTypeName has a similar factory method
            datetime.fromisoformat(data['occurred_at']),
            entity.make(data['data']),  # Assuming each entity class has a similar factory method
        )
