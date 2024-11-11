from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import (
    CatalogType,
    CustomData,
    Duration,
    ImportMeta,
    Money,
    PriceQuantity,
    Status,
    TaxMode,
    UnitPriceOverride,
)


@dataclass
class TransactionPreviewPrice(Entity):
    id: str | None
    product_id: str | None
    name: str | None
    description: str
    type: CatalogType
    billing_cycle: Duration | None
    trial_period: Duration | None
    tax_mode: TaxMode
    unit_price: Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity: PriceQuantity
    status: Status
    custom_data: CustomData | None
    import_meta: ImportMeta | None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict) -> TransactionPreviewPrice:
        return TransactionPreviewPrice(
            id=data.get("id"),
            product_id=data.get("product_id"),
            name=data.get("name"),
            description=data["description"],
            unit_price=Money.from_dict(data["unit_price"]),
            quantity=PriceQuantity.from_dict(data["quantity"]),
            status=Status(data["status"]),
            tax_mode=TaxMode(data.get("tax_mode")),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            unit_price_overrides=[
                UnitPriceOverride.from_dict(override) for override in data.get("unit_price_overrides", [])
            ],
            type=CatalogType(data.get("type")) if data.get("type") else None,
            billing_cycle=Duration.from_dict(data["billing_cycle"]) if data.get("billing_cycle") else None,
            trial_period=Duration.from_dict(data["trial_period"]) if data.get("trial_period") else None,
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            import_meta=ImportMeta.from_dict(data["import_meta"]) if data.get("import_meta") else None,
        )
