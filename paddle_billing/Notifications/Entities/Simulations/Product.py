from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import CatalogType, CustomData, ImportMeta, Status, TaxCategory
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Product(SimulationEntity):
    id: str | Undefined = Undefined()
    name: str | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    tax_category: TaxCategory | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    image_url: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    type: CatalogType | None | Undefined = Undefined()
    created_at: datetime | None | Undefined = Undefined()
    updated_at: datetime | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Product:
        return Product(
            description=data.get("description", Undefined()),
            id=data.get("id", Undefined()),
            image_url=data.get("image_url", Undefined()),
            name=data.get("name", Undefined()),
            status=Status(data["status"]) if data.get("status") else Undefined(),
            tax_category=TaxCategory(data["tax_category"]) if data.get("tax_category") else Undefined(),
            type=CatalogType(data["type"]) if data.get("type") else data.get("type", Undefined()),
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
            created_at=(
                datetime.fromisoformat(data["created_at"])
                if data.get("created_at")
                else data.get("created_at", Undefined())
            ),
            updated_at=(
                datetime.fromisoformat(data["updated_at"])
                if data.get("updated_at")
                else data.get("updated_at", Undefined())
            ),
        )
