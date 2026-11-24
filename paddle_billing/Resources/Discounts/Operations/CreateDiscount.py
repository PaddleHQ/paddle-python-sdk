from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.DateTime import DateTime as DateTime
from paddle_billing.Entities.Discounts import DiscountMode as DiscountMode, DiscountType as DiscountType
from paddle_billing.Entities.Shared import CurrencyCode as CurrencyCode, CustomData as CustomData


@dataclass
class CreateDiscount(Operation):
    amount: str
    description: str
    type: DiscountType
    enabled_for_checkout: bool
    recur: bool
    currency_code: CurrencyCode | None | Undefined = Undefined()
    code: str | None | Undefined = Undefined()
    maximum_recurring_intervals: int | None | Undefined = Undefined()
    usage_limit: int | None | Undefined = Undefined()
    restrict_to: list[str] | None | Undefined = Undefined()
    expires_at: DateTime | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    mode: DiscountMode | None | Undefined = Undefined()
    discount_group_id: str | None | Undefined = Undefined()
