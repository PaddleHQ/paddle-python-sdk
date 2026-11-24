from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation


@dataclass
class CreateDiscountGroup(Operation):
    name: str
