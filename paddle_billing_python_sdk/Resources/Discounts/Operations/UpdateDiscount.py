from dataclasses import asdict, dataclass

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Discounts.DiscountStatus import DiscountStatus
from paddle_billing_python_sdk.Entities.Discounts.DiscountType   import DiscountType
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode      import CurrencyCode


@dataclass
class UpdateDiscount:
    amount:                      str                   | Undefined = Undefined()
    description:                 str                   | Undefined = Undefined()
    type:                        DiscountType          | Undefined = Undefined()
    enabled_for_checkout:        bool                  | Undefined = Undefined()
    recur:                       bool                  | Undefined = Undefined()
    currency_code:               CurrencyCode          | Undefined = Undefined()
    code:                        str            | None | Undefined = Undefined()
    maximum_recurring_intervals: int            | None | Undefined = Undefined()
    usage_limit:                 int            | None | Undefined = Undefined()
    restrict_to:                 list[str]      | None | Undefined = Undefined()
    expires_at:                  str            | None | Undefined = Undefined()
    status:                      DiscountStatus | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
