from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Shared.CatalogType       import CatalogType
from paddle_billing.Entities.Shared.CustomData        import CustomData
from paddle_billing.Entities.Shared.Money             import Money
from paddle_billing.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing.Entities.Shared.TaxMode           import TaxMode
from paddle_billing.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class CreatePrice:
    description:          str
    product_id:           str
    unit_price:           Money
    name:                 str                     | None | Undefined = Undefined()
    type:                 CatalogType             | None | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | None | Undefined = Undefined()
    tax_mode:             TaxMode                 | None | Undefined = Undefined()
    trial_period:         TimePeriod              | None | Undefined = Undefined()
    billing_cycle:        TimePeriod              | None | Undefined = Undefined()
    quantity:             PriceQuantity           | None | Undefined = Undefined()
    custom_data:          CustomData              | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
