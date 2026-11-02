from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Settings.CheckoutRecoveryDiscountType import CheckoutRecoveryDiscountType


@dataclass
class CheckoutRecoveryDiscount:
    type: CheckoutRecoveryDiscountType
    amount: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutRecoveryDiscount:
        return CheckoutRecoveryDiscount(
            type=CheckoutRecoveryDiscountType(data["type"]),
            amount=data["amount"],
        )
