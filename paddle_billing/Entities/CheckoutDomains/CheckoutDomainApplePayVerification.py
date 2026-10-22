from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.CheckoutDomains.CheckoutDomainPaymentMethodVerificationStatus import (
    CheckoutDomainPaymentMethodVerificationStatus,
)


@dataclass
class CheckoutDomainApplePayVerification:
    status: CheckoutDomainPaymentMethodVerificationStatus

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutDomainApplePayVerification:
        return CheckoutDomainApplePayVerification(
            status=CheckoutDomainPaymentMethodVerificationStatus(data["status"]),
        )
