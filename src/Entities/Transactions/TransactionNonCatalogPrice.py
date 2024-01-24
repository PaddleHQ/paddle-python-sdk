from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TimePeriod        import TimePeriod
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.CustomData        import CustomData
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class TransactionNonCatalogPrice:
    description:          str
    name:                 str | None
    billing_cycle:        TimePeriod | None
    trial_period:         TimePeriod | None
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    custom_data:          CustomData | None
    product_id:           str


    @staticmethod
    def from_dict(data: dict) -> TransactionNonCatalogPrice:
        return TransactionNonCatalogPrice(
            description          = data['description'],
            name                 = data.get('name'),
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if 'billing_cycle' in data else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if 'trial_period'  in data else None,
            tax_mode             = data['tax_mode'],
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(item) for item in data['unit_price_overrides']],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            custom_data          = CustomData(data['custom_data']) if 'custom_data' in data else None,
            product_id           = data['product_id'],
        )
