from __future__ import annotations
from typing import Any
from dataclasses import dataclass
from abc import ABC
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity
from importlib import import_module


@dataclass
class SimulationEntity(ABC):
    @staticmethod
    def from_dict_for_event_type(data: dict[str, Any], event_type: str) -> SimulationEntity | UndefinedEntity:
        entity_class_name = SimulationEntity._resolve_event_class_name(event_type)

        entity_class = None
        instantiated_class = None
        entity_module_path = "paddle_billing.Notifications.Entities.Simulations"

        try:
            imported_module = import_module(f"{entity_module_path}.{entity_class_name}")
            entity_class = getattr(imported_module, entity_class_name)

            instantiated_class = entity_class.from_dict(data)
        except Exception as error:
            print(f"Error dynamically instantiating a '{entity_module_path}.{entity_class_name}' object: {error}")

        if not instantiated_class:
            return UndefinedEntity(data)

        if entity_class is None or not issubclass(entity_class, SimulationEntity):
            raise ValueError(f"Event type '{entity_class_name}' is not of SimulationEntity")

        return instantiated_class

    @staticmethod
    def _resolve_event_class_name(event_type) -> str:
        if event_type == "subscription.created":
            return "SubscriptionCreated"
        if event_type == "payment_method.deleted":
            return "PaymentMethodDeleted"

        event_entity = event_type.split(".")[0] or ""

        return event_entity.lower().title().replace("_", "")
