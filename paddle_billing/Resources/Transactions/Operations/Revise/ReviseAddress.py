from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class ReviseAddress(Operation):
    first_line: str | Undefined = Undefined()
    second_line: str | None | Undefined = Undefined()
    city: str | Undefined = Undefined()
    region: str | Undefined = Undefined()
