from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import (
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

from paddle_billing.Logger import get_logger

log = get_logger()


@dataclass
class Price(Entity):
    id: str
    product_id: str
    name: str | None
    description: str
    type: CatalogType | None
    billing_cycle: Duration | None
    trial_period: Duration | None
    tax_mode: TaxMode
    unit_price: Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity: PriceQuantity
    status: Status
    custom_data: CustomData | None
    import_meta: ImportMeta | None
    created_at: datetime | None
    updated_at: datetime | None

    @classmethod
    def from_dict(cls, data: dict) -> Price:
        return Price(
            id=data["id"],
            product_id=data["product_id"],
            name=data.get("name"),
            description=data["description"],
            unit_price=Money.from_dict(data["unit_price"]),
            quantity=PriceQuantity.from_dict(data["quantity"]),
            status=Status(data["status"]),
            tax_mode=TaxMode(data.get("tax_mode")),
            unit_price_overrides=[
                UnitPriceOverride.from_dict(override) for override in data.get("unit_price_overrides", [])
            ],
            type=CatalogType(data.get("type")) if data.get("type") else None,
            billing_cycle=Duration.from_dict(data["billing_cycle"]) if data.get("billing_cycle") else None,
            trial_period=Duration.from_dict(data["trial_period"]) if data.get("trial_period") else None,
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            import_meta=ImportMeta.from_dict(data["import_meta"]) if data.get("import_meta") else None,
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None,
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else None,
        )


# Prevents circular import
from paddle_billing.Entities.Product import Product  # noqa E402
