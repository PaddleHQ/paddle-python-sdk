from dataclasses import dataclass

from paddle_billing.Entities.Settings.CheckoutRecoveryDiscountType import CheckoutRecoveryDiscountType


@dataclass
class CheckoutRecoveryDiscountUpdate:
    type: CheckoutRecoveryDiscountType
    amount: str
