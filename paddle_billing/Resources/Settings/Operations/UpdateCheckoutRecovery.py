from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Settings import CheckoutRecoveryDiscountUpdate


@dataclass
class UpdateCheckoutRecovery(Operation):
    enabled: bool | Undefined = Undefined()
    discount: CheckoutRecoveryDiscountUpdate | None | Undefined = Undefined()
