from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class ReviseBusiness(Operation):
    name: str | Undefined = Undefined()
    tax_identifier: str | Undefined = Undefined()
