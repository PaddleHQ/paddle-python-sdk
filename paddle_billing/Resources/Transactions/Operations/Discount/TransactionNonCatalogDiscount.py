from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared.CustomData import CustomData
from paddle_billing.Entities.Discounts.DiscountType import DiscountType


@dataclass
class TransactionNonCatalogDiscount:
    amount: str
    description: str
    type: DiscountType
    recur: bool | Undefined = Undefined()
    maximum_recurring_intervals: int | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    restrict_to: list[str] | None | Undefined = Undefined()
