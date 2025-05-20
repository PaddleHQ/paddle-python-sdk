from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared import CurrencyCode


@dataclass
class SubscriptionCharge:
    amount: str
    currency_code: CurrencyCode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCharge:
        return SubscriptionCharge(
            amount=data["amount"],
            currency_code=CurrencyCode(data["currency_code"]),
        )
