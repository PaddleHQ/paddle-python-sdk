from __future__ import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode

from src.Entities.Subscriptions.SubscriptionResultAction import SubscriptionResultAction


@dataclass
class SubscriptionResult:
    action:       SubscriptionResultAction
    amount:       str
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> SubscriptionResult:
        return SubscriptionResult(
            action       = SubscriptionResultAction(data['action']),
            amount       = data['amount'],
            currency_code = CurrencyCode(data['currency_code']),
        )
