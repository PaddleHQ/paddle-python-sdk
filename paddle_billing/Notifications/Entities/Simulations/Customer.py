from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import CustomData, ImportMeta, Status
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Customer(SimulationEntity):
    id: str | Undefined = Undefined()
    name: str | None | Undefined = Undefined()
    email: str | Undefined = Undefined()
    marketing_consent: bool | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    locale: str | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict) -> Customer:
        return Customer(
            id=data.get("id", Undefined()),
            name=data.get("name", Undefined()),
            email=data.get("email", Undefined()),
            marketing_consent=data.get("marketing_consent", Undefined()),
            status=Status(data["status"]) if data.get("status") else Undefined(),
            locale=data.get("locale", Undefined()),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            custom_data=(
                CustomData(data["custom_data"])
                if isinstance(data.get("custom_data"), dict)
                else data.get("custom_data", Undefined())
            ),
            import_meta=(
                ImportMeta.from_dict(data["import_meta"])
                if isinstance(data.get("import_meta"), dict)
                else data.get("import_meta", Undefined())
            ),
        )
