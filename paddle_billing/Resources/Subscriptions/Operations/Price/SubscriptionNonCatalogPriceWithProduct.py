from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared.CustomData import CustomData as CustomData
from paddle_billing.Entities.Shared.Money import Money as Money
from paddle_billing.Entities.Shared.PriceQuantity import PriceQuantity as PriceQuantity
from paddle_billing.Entities.Shared.TaxMode import TaxMode as TaxMode
from paddle_billing.Entities.Shared.Duration import Duration as Duration
from paddle_billing.Entities.Shared.PriceTrialPeriod import PriceTrialPeriod as PriceTrialPeriod
from paddle_billing.Entities.Shared.UnitPriceOverride import UnitPriceOverride as UnitPriceOverride

from paddle_billing.Resources.Subscriptions.Operations.Price.SubscriptionNonCatalogProduct import (
    SubscriptionNonCatalogProduct as SubscriptionNonCatalogProduct,
)


@dataclass
class SubscriptionNonCatalogPriceWithProduct:
    description: str
    unit_price: Money
    product: SubscriptionNonCatalogProduct
    name: str | None | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    trial_period: PriceTrialPeriod | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
