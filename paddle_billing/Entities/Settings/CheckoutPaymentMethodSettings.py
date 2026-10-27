from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.CheckoutPaymentMethods import CheckoutPaymentMethods


@dataclass
class CheckoutPaymentMethodSettings(Entity):
    payment_methods: CheckoutPaymentMethods

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutPaymentMethodSettings:
        return CheckoutPaymentMethodSettings(
            payment_methods=CheckoutPaymentMethods.from_dict(data["payment_methods"]),
        )
