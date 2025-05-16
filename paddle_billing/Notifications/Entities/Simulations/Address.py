from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import CountryCode, CustomData, ImportMeta, Status
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Address(SimulationEntity):
    id: str | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    first_line: str | None | Undefined = Undefined()
    second_line: str | None | Undefined = Undefined()
    city: str | None | Undefined = Undefined()
    postal_code: str | None | Undefined = Undefined()
    region: str | None | Undefined = Undefined()
    country_code: CountryCode | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    customer_id: str | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Address:
        return Address(
            id=data.get("id", Undefined()),
            customer_id=data.get("customer_id", Undefined()),
            description=data.get("description", Undefined()),
            first_line=data.get("first_line", Undefined()),
            second_line=data.get("second_line", Undefined()),
            city=data.get("city", Undefined()),
            postal_code=data.get("postal_code", Undefined()),
            region=data.get("region", Undefined()),
            country_code=CountryCode(data["country_code"]) if data.get("country_code") else Undefined(),
            status=Status(data["status"]) if data.get("status") else Undefined(),
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
