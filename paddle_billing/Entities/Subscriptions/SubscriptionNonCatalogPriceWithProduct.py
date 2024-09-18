from __future__  import annotations
from dataclasses import asdict, dataclass

from paddle_billing.Entities.Shared import CustomData, Money, PriceQuantity, TaxMode, UnitPriceOverride, TimePeriod

from paddle_billing.Entities.Subscriptions.SubscriptionNonCatalogProduct import SubscriptionNonCatalogProduct


@dataclass
class SubscriptionNonCatalogPriceWithProduct:
    description:          str
    name:                 str | None
    product:              SubscriptionNonCatalogProduct
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    custom_data:          CustomData | None
    billing_cycle:        TimePeriod | None
    trial_period:         TimePeriod | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogPriceWithProduct:
        return SubscriptionNonCatalogPriceWithProduct(
            description          = data['description'],
            name                 = data.get('name'),
            product              = SubscriptionNonCatalogProduct.from_dict(data['product']),
            tax_mode             = TaxMode(data['tax_mode']),
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data['unit_price_overrides']],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            custom_data          = CustomData(data['custom_data']) if data.get('custom_data') else None,
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if data.get('billing_cycle') else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if data.get('trial_period')  else None,
        )


    def get_parameters(self) -> dict:
        parameters = asdict(self)

        if isinstance(self.product, SubscriptionNonCatalogProduct):
            parameters['product'] = self.product.get_parameters()

        if isinstance(self.custom_data, CustomData):
            parameters['custom_data'] = self.custom_data.get_parameters()

        return parameters
