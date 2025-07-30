from dataclasses import dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.DiscountGroup import DiscountGroupStatus
from paddle_billing.Operation import Operation


@dataclass
class UpdateDiscountGroup(Operation):
    name: str | Undefined = Undefined()
    status: DiscountGroupStatus | Undefined = Undefined()
