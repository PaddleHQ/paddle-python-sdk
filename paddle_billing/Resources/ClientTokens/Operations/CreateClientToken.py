from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class CreateClientToken(Operation):
    name: str
    description: str | None | Undefined = Undefined()
