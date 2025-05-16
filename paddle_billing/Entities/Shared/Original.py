from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.CurrencyCodeAdjustments import CurrencyCodeAdjustments


@dataclass
class Original:
    amount: str
    currency_code: CurrencyCodeAdjustments

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Original:
        return Original(
            amount=data["amount"],
            currency_code=CurrencyCodeAdjustments(data["currency_code"]),
        )
