from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import CurrencyCode

from paddle_billing.Entities.Subscriptions.SubscriptionResultAction import SubscriptionResultAction


@dataclass
class SubscriptionResult:
    action:        SubscriptionResultAction
    amount:        str
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> SubscriptionResult:
        return SubscriptionResult(
            action        = SubscriptionResultAction(data['action']),
            amount        = data['amount'],
            currency_code = CurrencyCode(data['currency_code']),
        )
