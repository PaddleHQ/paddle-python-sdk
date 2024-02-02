from dataclasses import asdict, dataclass

from paddle_billing.Undefined          import Undefined
from paddle_billing.Entities.Discounts import DiscountType
from paddle_billing.Entities.Shared    import CurrencyCode


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
