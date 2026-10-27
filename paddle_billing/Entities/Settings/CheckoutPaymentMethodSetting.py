from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class CheckoutPaymentMethodSetting:
    enabled: bool
    available: bool

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutPaymentMethodSetting:
        return CheckoutPaymentMethodSetting(
            enabled=data["enabled"],
            available=data["available"],
        )
