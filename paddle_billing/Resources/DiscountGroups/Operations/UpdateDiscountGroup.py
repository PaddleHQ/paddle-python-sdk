from dataclasses import dataclass

from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.DiscountGroup import DiscountGroupStatus as DiscountGroupStatus
from paddle_billing.Operation import Operation as Operation


@dataclass
class UpdateDiscountGroup(Operation):
    name: str | Undefined = Undefined()
    status: DiscountGroupStatus | Undefined = Undefined()
