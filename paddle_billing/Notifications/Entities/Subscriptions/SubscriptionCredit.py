from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared import CurrencyCode


@dataclass
class SubscriptionCredit:
    amount:        str
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> SubscriptionCredit:
        return SubscriptionCredit(
            amount        = data['amount'],
            currency_code = CurrencyCode(data['currency_code']),
        )
