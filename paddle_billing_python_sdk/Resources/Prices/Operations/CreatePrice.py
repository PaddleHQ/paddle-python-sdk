from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Entities.Shared.CatalogType       import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData
from paddle_billing_python_sdk.Entities.Shared.Money             import Money
from paddle_billing_python_sdk.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing_python_sdk.Entities.Shared.TaxMode           import TaxMode
from paddle_billing_python_sdk.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing_python_sdk.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class CreatePrice:
    description:          str
    product_id:           str
    unit_price:           Money
    name:                 str | None                     = None
    type:                 CatalogType | None             = None
    unit_price_overrides: list[UnitPriceOverride] | None = None
    tax_mode:             TaxMode | None                 = None
    trial_period:         TimePeriod | None              = None
    billing_cycle:        TimePeriod | None              = None
    quantity:             PriceQuantity | None           = None
    custom_data:          CustomData | None              = None


    def get_parameters(self) -> dict:
        return asdict(self)
