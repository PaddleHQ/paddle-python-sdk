from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.CustomData        import CustomData
from paddle_billing.Entities.Shared.Money             import Money
from paddle_billing.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing.Entities.Shared.TaxMode           import TaxMode
from paddle_billing.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing.Entities.Shared.UnitPriceOverride import UnitPriceOverride

from paddle_billing.Entities.Transactions.TransactionNonCatalogProduct import TransactionNonCatalogProduct


@dataclass
class TransactionNonCatalogPriceWithProduct:
    description:          str
    name:                 str        | None
    billing_cycle:        TimePeriod | None
    trial_period:         TimePeriod | None
    custom_data:          CustomData | None
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    product:              TransactionNonCatalogProduct


    @staticmethod
    def from_dict(data: dict) -> TransactionNonCatalogPriceWithProduct:
        return TransactionNonCatalogPriceWithProduct(
            description          = data['description'],
            name                 = data.get('name'),
            tax_mode             = data['tax_mode'],
            unit_price           = Money.from_dict(data['unit_price']),
            quantity             = PriceQuantity.from_dict(data['quantity']),
            product              = TransactionNonCatalogProduct.from_dict(data['product_id']),
            unit_price_overrides = [UnitPriceOverride.from_dict(item) for item in data['unit_price_overrides']],
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if data.get('billing_cycle') else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if data.get('trial_period')  else None,
            custom_data          = CustomData(data['custom_data'])             if data.get('custom_data')   else None,
        )
