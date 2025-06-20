from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Discounts import DiscountMode, DiscountType
from paddle_billing.Entities.Shared import CurrencyCode, CustomData


@dataclass
class CreateDiscount(Operation):
    amount: str
    description: str
    type: DiscountType
    enabled_for_checkout: bool
    recur: bool
    currency_code: CurrencyCode
    code: str | None | Undefined = Undefined()
    maximum_recurring_intervals: int | None | Undefined = Undefined()
    usage_limit: int | None | Undefined = Undefined()
    restrict_to: list[str] | None | Undefined = Undefined()
    expires_at: DateTime | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    mode: DiscountMode | None | Undefined = Undefined()
    discount_group_id: str | None | Undefined = Undefined()
