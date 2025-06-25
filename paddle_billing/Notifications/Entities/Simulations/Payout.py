from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Payouts import PayoutStatus
from paddle_billing.Notifications.Entities.Shared import CurrencyCodePayouts
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Payout(SimulationEntity):
    amount: str | Undefined = Undefined()
    currency_code: CurrencyCodePayouts | Undefined = Undefined()
    id: str | Undefined = Undefined()
    status: PayoutStatus | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Payout:
        return Payout(
            amount=data.get("amount", Undefined()),
            id=data.get("id", Undefined()),
            status=PayoutStatus(data["status"]) if data.get("status") else Undefined(),
            currency_code=CurrencyCodePayouts(data["currency_code"]) if data.get("currency_code") else Undefined(),
        )
