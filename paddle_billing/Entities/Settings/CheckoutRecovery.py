from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.CheckoutRecoveryDiscount import CheckoutRecoveryDiscount


@dataclass
class CheckoutRecovery(Entity):
    enabled: bool
    discount: CheckoutRecoveryDiscount | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutRecovery:
        return CheckoutRecovery(
            enabled=data["enabled"],
            discount=CheckoutRecoveryDiscount.from_dict(data["discount"]) if data["discount"] is not None else None,
        )
