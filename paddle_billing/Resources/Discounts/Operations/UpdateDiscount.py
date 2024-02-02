from dataclasses import asdict, dataclass

from paddle_billing.Undefined          import Undefined
from paddle_billing.Entities.Discounts import DiscountStatus, DiscountType
from paddle_billing.Entities.Shared    import CurrencyCode


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
    status:                      DiscountStatus        | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
