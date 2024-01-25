from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Entities.Shared.CatalogType       import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData
from paddle_billing_python_sdk.Entities.Shared.Money             import Money
from paddle_billing_python_sdk.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing_python_sdk.Entities.Shared.Status            import Status
from paddle_billing_python_sdk.Entities.Shared.TaxMode           import TaxMode
from paddle_billing_python_sdk.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing_python_sdk.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class UpdatePrice:
    description:          str | None                     = None
    name:                 str | None                     = None
    type:                 CatalogType | None             = None
    billing_cycle:        TimePeriod | None              = None
    tax_mode:             TaxMode | None                 = None
    unit_price:           Money | None                   = None
    unit_price_overrides: list[UnitPriceOverride] | None = None
    quantity:             PriceQuantity | None           = None
    status:               Status | None                  = None
    custom_data:          CustomData | None              = None


    def get_parameters(self) -> dict:
        return asdict(self)
