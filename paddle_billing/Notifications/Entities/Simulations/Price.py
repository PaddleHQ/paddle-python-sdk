from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Undefined import Undefined
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
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Price(SimulationEntity):
    id: str | Undefined = Undefined()
    product_id: str | Undefined = Undefined()
    name: str | None | Undefined = Undefined()
    description: str | Undefined = Undefined()
    type: CatalogType | None | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    trial_period: Duration | None | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    unit_price: Money | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    created_at: datetime | None | Undefined = Undefined()
    updated_at: datetime | None | Undefined = Undefined()

    @classmethod
    def from_dict(cls, data: dict) -> Price:
        return Price(
            id=data.get("id", Undefined()),
            product_id=data.get("product_id", Undefined()),
            name=data.get("name", Undefined()),
            description=data.get("description", Undefined()),
            unit_price=Money.from_dict(data["unit_price"]) if data.get("unit_price") else Undefined(),
            quantity=PriceQuantity.from_dict(data["quantity"]) if data.get("quantity") else Undefined(),
            status=Status(data["status"]) if data.get("status") else Undefined(),
            tax_mode=TaxMode(data.get("tax_mode")) if data.get("tax_mode") else Undefined(),
            unit_price_overrides=(
                [UnitPriceOverride.from_dict(override) for override in data.get("unit_price_overrides", [])]
                if isinstance(data.get("unit_price_overrides"), list)
                else Undefined()
            ),
            type=CatalogType(data.get("type")) if data.get("type") else data.get("type", Undefined()),
            billing_cycle=(
                Duration.from_dict(data["billing_cycle"])
                if data.get("billing_cycle")
                else data.get("billing_cycle", Undefined())
            ),
            trial_period=(
                Duration.from_dict(data["trial_period"])
                if data.get("trial_period")
                else data.get("trial_period", Undefined())
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
