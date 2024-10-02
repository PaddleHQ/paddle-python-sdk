from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import (
    CatalogType,
    CustomData,
    Duration,
    Money,
    PriceQuantity,
    Status,
    TaxMode,
    UnitPriceOverride,
)


@dataclass
class UpdatePrice:
    description: str | Undefined = Undefined()
    name: str | None | Undefined = Undefined()
    type: CatalogType | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    trial_period: Duration | None | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    unit_price: Money | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
    status: Status | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()

    def get_parameters(self) -> dict:
        return asdict(self)
