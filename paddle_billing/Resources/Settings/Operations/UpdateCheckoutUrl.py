from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class UpdateCheckoutUrl(Operation):
    default_url: str | None | Undefined = Undefined()
