from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import CustomData, Duration, Money, PriceQuantity, TaxMode, UnitPriceOverride


@dataclass
class SubscriptionNonCatalogPrice:
    description: str
    name: str | None
    product_id: str
    tax_mode: TaxMode
    unit_price: Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity: PriceQuantity
    custom_data: CustomData | None
    billing_cycle: Duration | None
    trial_period: Duration | None

    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogPrice:
        return SubscriptionNonCatalogPrice(
            description=data["description"],
            name=data.get("name"),
            product_id=data["product_id"],
            tax_mode=TaxMode(data["tax_mode"]),
            unit_price=Money.from_dict(data["unit_price"]),
            unit_price_overrides=[UnitPriceOverride.from_dict(override) for override in data["unit_price_overrides"]],
            quantity=PriceQuantity.from_dict(data["quantity"]),
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            billing_cycle=Duration.from_dict(data["billing_cycle"]) if data.get("billing_cycle") else None,
            trial_period=Duration.from_dict(data["trial_period"]) if data.get("trial_period") else None,
        )
