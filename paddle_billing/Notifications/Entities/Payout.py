from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Payouts import PayoutStatus
from paddle_billing.Notifications.Entities.Shared import CurrencyCodePayouts


@dataclass
class Payout(Entity):
    amount: str
    currency_code: CurrencyCodePayouts
    id: str
    status: PayoutStatus
    remittance_reference: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Payout:
        return Payout(
            amount=data["amount"],
            id=data["id"],
            status=PayoutStatus(data["status"]),
            currency_code=CurrencyCodePayouts(data["currency_code"]),
            remittance_reference=data.get("remittance_reference"),
        )
