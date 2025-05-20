from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Businesses import BusinessesContacts
from paddle_billing.Notifications.Entities.Shared import CustomData, ImportMeta, Status
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Business(SimulationEntity):
    id: str | Undefined = Undefined()
    name: str | Undefined = Undefined()
    company_number: str | None | Undefined = Undefined()
    tax_identifier: str | None | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    contacts: list[BusinessesContacts] | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    customer_id: str | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Business:
        return Business(
            id=data.get("id", Undefined()),
            customer_id=data.get("customer_id", Undefined()),
            name=data.get("name", Undefined()),
            company_number=data.get("company_number", Undefined()),
            tax_identifier=data.get("tax_identifier", Undefined()),
            status=Status(data["status"]) if data.get("status") else Undefined(),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            contacts=(
                [BusinessesContacts.from_dict(contact) for contact in data["contacts"]]
                if data.get("contacts")
                else Undefined()
            ),
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
