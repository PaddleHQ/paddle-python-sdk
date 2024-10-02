from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import CountryCode, CustomData, ImportMeta, Status


@dataclass
class Address(Entity):
    id: str
    description: str | None
    first_line: str | None
    second_line: str | None
    city: str | None
    postal_code: str | None
    region: str | None
    country_code: CountryCode
    status: Status
    created_at: datetime
    updated_at: datetime
    custom_data: CustomData | None = None
    import_meta: ImportMeta | None = None
    customer_id: str | None = None

    @staticmethod
    def from_dict(data: dict) -> Address:
        return Address(
            id=data["id"],
            customer_id=data.get("customer_id"),
            description=data.get("description"),
            first_line=data.get("first_line"),
            second_line=data.get("second_line"),
            city=data.get("city"),
            postal_code=data.get("postal_code"),
            region=data.get("region"),
            country_code=CountryCode(data["country_code"]),
            status=Status(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            import_meta=ImportMeta.from_dict(data["import_meta"]) if data.get("import_meta") else None,
        )
