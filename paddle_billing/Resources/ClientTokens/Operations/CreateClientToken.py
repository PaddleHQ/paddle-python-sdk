from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class CreateClientToken(Operation):
    name: str
    description: str | None | Undefined = Undefined()
