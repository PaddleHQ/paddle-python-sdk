from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CustomData        import CustomData
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class SubscriptionNonCatalogPrice:
    description:          str
    name:                 str | None
    product_id:           str
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    custom_data:          CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogPrice:
        return SubscriptionNonCatalogPrice(
            description          = data['description'],
            name                 = data.get('name'),
            product_id           = data['product_id'],
            tax_mode             = TaxMode(data['tax_mode']),
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data['unit_price_overrides']],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            custom_data          = CustomData(data['custom_data']) if 'custom_data' in data else None,
        )
