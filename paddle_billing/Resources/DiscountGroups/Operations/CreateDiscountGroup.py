from dataclasses import dataclass

from paddle_billing.Operation import Operation


@dataclass
class CreateDiscountGroup(Operation):
    name: str
