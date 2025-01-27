from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class ReviseCustomer(Operation):
    name: str | Undefined = Undefined()
