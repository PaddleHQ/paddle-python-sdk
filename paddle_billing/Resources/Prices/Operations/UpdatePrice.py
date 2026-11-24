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
    Status as Status,
    TaxMode as TaxMode,
    UnitPriceOverride as UnitPriceOverride,
)


@dataclass
class UpdatePrice(Operation):
    description: str | Undefined = Undefined()
    name: str | None | Undefined = Undefined()
    type: CatalogType | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    trial_period: PriceTrialPeriod | None | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    unit_price: Money | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
