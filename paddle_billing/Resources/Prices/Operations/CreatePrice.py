from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared import (
    CatalogType as CatalogType,
    CustomData as CustomData,
    Duration as Duration,
    Money as Money,
    PriceQuantity as PriceQuantity,
    PriceTrialPeriod as PriceTrialPeriod,
    TaxMode as TaxMode,
    UnitPriceOverride as UnitPriceOverride,
)


@dataclass
class CreatePrice(Operation):
    description: str
    product_id: str
    unit_price: Money
    name: str | None | Undefined = Undefined()
    type: CatalogType | None | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    trial_period: PriceTrialPeriod | None | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
    custom_data: CustomData | Undefined = Undefined()
