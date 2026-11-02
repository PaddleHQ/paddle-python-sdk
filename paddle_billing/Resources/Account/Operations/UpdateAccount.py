from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class UpdateAccount(Operation):
    email: str | Undefined = Undefined()
