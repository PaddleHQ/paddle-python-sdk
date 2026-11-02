from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class UpdateCheckoutStylesOverlay(Operation):
    primary_checkout_color: str | None | Undefined = Undefined()
