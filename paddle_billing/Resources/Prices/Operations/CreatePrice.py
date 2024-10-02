from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import (
    CatalogType,
    CustomData,
    Duration,
    Money,
    PriceQuantity,
    TaxMode,
    UnitPriceOverride,
)


@dataclass
class CreatePrice:
    description: str
    product_id: str
    unit_price: Money
    name: str | None | Undefined = Undefined()
    type: CatalogType | None | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()
    tax_mode: TaxMode | Undefined = Undefined()
    trial_period: Duration | None | Undefined = Undefined()
    billing_cycle: Duration | None | Undefined = Undefined()
    quantity: PriceQuantity | Undefined = Undefined()
    custom_data: CustomData | Undefined = Undefined()

    def get_parameters(self) -> dict:
        return asdict(self)
