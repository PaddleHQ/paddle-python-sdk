from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Discounts.DiscountType import DiscountType
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode    import CurrencyCode


@dataclass
class CreateDiscount:
    amount:                      str
    description:                 str
    type:                        DiscountType
    enabled_for_checkout:        bool
    recur:                       bool
    currency_code:               CurrencyCode
    code:                        str       | None | Undefined = Undefined()
    maximum_recurring_intervals: int       | None | Undefined = Undefined()
    usage_limit:                 int       | None | Undefined = Undefined()
    restrict_to:                 list[str] | None | Undefined = Undefined()
    expires_at:                  str       | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
