from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared.CustomData import CustomData
from paddle_billing.Entities.Shared.Money import Money
from paddle_billing.Entities.Shared.PriceQuantity import PriceQuantity
from paddle_billing.Entities.Shared.TaxMode import TaxMode
from paddle_billing.Entities.Shared.Duration import Duration
from paddle_billing.Entities.Shared.UnitPriceOverride import UnitPriceOverride

from paddle_billing.Resources.Subscriptions.Operations.Price import (
    SubscriptionNonCatalogProduct,
)


@dataclass
class SubscriptionNonCatalogPriceWithProduct:
    description: str
    unit_price: Money
    product: SubscriptionNonCatalogProduct
    name: str | None | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    trial_period: Duration | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
