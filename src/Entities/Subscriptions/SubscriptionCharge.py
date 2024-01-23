from __future__ import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class SubscriptionCharge:
    amount:       str
    currencyCode: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> SubscriptionCharge:
        return SubscriptionCharge(
            amount       = data['amount'],
            currencyCode = CurrencyCode(data['currency_code']),
        )
