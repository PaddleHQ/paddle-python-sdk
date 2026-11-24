from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Settings import CheckoutRecoveryDiscountUpdate as CheckoutRecoveryDiscountUpdate


@dataclass
class UpdateCheckoutRecovery(Operation):
    enabled: bool | Undefined = Undefined()
    discount: CheckoutRecoveryDiscountUpdate | None | Undefined = Undefined()
