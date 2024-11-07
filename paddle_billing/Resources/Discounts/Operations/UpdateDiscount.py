from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Discounts import DiscountStatus, DiscountType
from paddle_billing.Entities.Shared import CurrencyCode, CustomData


@dataclass
class UpdateDiscount(Operation):
    amount: str | Undefined = Undefined()
    description: str | Undefined = Undefined()
    type: DiscountType | Undefined = Undefined()
    enabled_for_checkout: bool | Undefined = Undefined()
    recur: bool | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    code: str | None | Undefined = Undefined()
    maximum_recurring_intervals: int | None | Undefined = Undefined()
    usage_limit: int | None | Undefined = Undefined()
    restrict_to: list[str] | None | Undefined = Undefined()
    expires_at: DateTime | None | Undefined = Undefined()
    status: DiscountStatus | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
