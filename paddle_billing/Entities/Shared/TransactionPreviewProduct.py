from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import CatalogType, CustomData, ImportMeta, Status, TaxCategory


@dataclass
class TransactionPreviewProduct(Entity):
    id: str | None
    name: str
    description: str | None
    tax_category: TaxCategory
    image_url: str | None
    status: Status
    created_at: datetime
    updated_at: datetime
    type: CatalogType | None = None
    custom_data: CustomData | None = None
    import_meta: ImportMeta | None = None

    @staticmethod
    def from_dict(data: dict) -> TransactionPreviewProduct:
        return TransactionPreviewProduct(
            id=data.get("id"),
            name=data["name"],
            description=data.get("description"),
            tax_category=TaxCategory(data["tax_category"]),
            image_url=data.get("image_url"),
            status=Status(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            type=CatalogType(data["type"]) if data.get("type") else None,
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            import_meta=ImportMeta.from_dict(data["import_meta"]) if data.get("import_meta") else None,
        )
