from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import (
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class PaymentMethod(SimulationEntity):
    id: str | Undefined = Undefined()
    customer_id: str | Undefined = Undefined()
    address_id: str | Undefined = Undefined()
    type: SavedPaymentMethodType | Undefined = Undefined()
    origin: SavedPaymentMethodOrigin | Undefined = Undefined()
    saved_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict) -> PaymentMethod:
        return PaymentMethod(
            id=data.get("id", Undefined()),
            customer_id=data.get("customer_id", Undefined()),
            address_id=data.get("address_id", Undefined()),
            type=SavedPaymentMethodType(data["type"]) if data.get("type") else Undefined(),
            origin=SavedPaymentMethodOrigin(data["origin"]) if data.get("origin") else Undefined(),
            saved_at=datetime.fromisoformat(data["saved_at"]) if data.get("saved_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
        )
