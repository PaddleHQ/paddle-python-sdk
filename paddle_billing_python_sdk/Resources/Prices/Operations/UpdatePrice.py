from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

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
    description:          str | None                     = Undefined()
    name:                 str | None                     = Undefined()
    type:                 CatalogType | None             = Undefined()
    billing_cycle:        TimePeriod | None              = Undefined()
    tax_mode:             TaxMode | None                 = Undefined()
    unit_price:           Money | None                   = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | None = Undefined()
    quantity:             PriceQuantity | None           = Undefined()
    status:               Status | None                  = Undefined()
    custom_data:          CustomData | None              = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
