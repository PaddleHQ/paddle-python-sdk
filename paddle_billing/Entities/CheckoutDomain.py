from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.CheckoutDomains import CheckoutDomainPaymentMethodVerification, CheckoutDomainStatus


@dataclass
class CheckoutDomain(Entity):
    id: str
    domain: str
    status: CheckoutDomainStatus
    payment_method_verification: CheckoutDomainPaymentMethodVerification
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutDomain:
        return CheckoutDomain(
            id=data["id"],
            domain=data["domain"],
            status=CheckoutDomainStatus(data["status"]),
            payment_method_verification=CheckoutDomainPaymentMethodVerification.from_dict(
                data["payment_method_verification"]
            ),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
