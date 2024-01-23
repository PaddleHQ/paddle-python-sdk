# TODO this is not done

from src.Entities.Adjustment                            import Adjustment
from src.Entities.Entity                                import Entity
from src.Entities.Event.EventTypeName                   import EventTypeName
from src.Entities.Notification.NotificationDiscount     import NotificationDiscount
from src.Entities.Notification.NotificationSubscription import NotificationSubscription
from dataclasses                                        import dataclass
from datetime                                           import datetime
from abc                                                import ABC, abstractmethod


@dataclass
class Event(Entity):  # Assuming Entity is already defined as an ABC
    eventId:    str
    eventType:  EventTypeName
    occurredAt: datetime
    data:       Entity


    @classmethod
    def from_dict(cls, data: dict):
        type_ = data['event_type'].split('.')[0] or ''

        def entity_mapping(event_type):
            match event_type:
                case "discount":
                    return NotificationDiscount
                case "subscription":
                    return NotificationSubscription
                case _:
                    return str(event_type).title()

        event_type_str = data['event_type'].split('.')[0].lower()
        entity_mapping = entity_mapping(type)
        entity_class   = entity_mapping(event_type_str)

        if not entity_class:
            raise ValueError(f"Event type '{event_type_str}' cannot be mapped to an object")

        entity = None  # TODO do import module stuff here
        if not issubclass(entity, Entity):
            raise ValueError(f"Event type '{type_}' cannot be mapped to an object")

        return cls(
            data['event_id'],
            EventTypeName(data['event_type']),  # Assuming EventTypeName has a similar factory method
            datetime.fromisoformat(data['occurred_at']),
            entity.from_dict(data['data']),  # Assuming each entity class has a similar factory method
        )
