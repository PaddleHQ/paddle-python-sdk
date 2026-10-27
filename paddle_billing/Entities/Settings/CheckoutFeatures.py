from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.AudienceOptIn import AudienceOptIn


@dataclass
class CheckoutFeatures(Entity):
    discounts_enabled: bool
    audience_opt_in: AudienceOptIn
    saved_payment_methods_enabled: bool

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutFeatures:
        return CheckoutFeatures(
            discounts_enabled=data["discounts_enabled"],
            audience_opt_in=AudienceOptIn(data["audience_opt_in"]),
            saved_payment_methods_enabled=data["saved_payment_methods_enabled"],
        )
