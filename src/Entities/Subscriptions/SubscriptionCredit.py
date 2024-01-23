from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class SubscriptionCredit:
    amount:       str
    currencyCode: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> SubscriptionCredit:
        return SubscriptionCredit(
            amount       = data['amount'],
            currencyCode = CurrencyCode(data['currency_code']),
        )
