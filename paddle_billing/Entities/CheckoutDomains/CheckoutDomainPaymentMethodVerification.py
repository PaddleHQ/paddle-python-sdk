from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.CheckoutDomains.CheckoutDomainApplePayVerification import (
    CheckoutDomainApplePayVerification,
)


@dataclass
class CheckoutDomainPaymentMethodVerification:
    apple_pay: CheckoutDomainApplePayVerification

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutDomainPaymentMethodVerification:
        return CheckoutDomainPaymentMethodVerification(
            apple_pay=CheckoutDomainApplePayVerification.from_dict(data["apple_pay"]),
        )
