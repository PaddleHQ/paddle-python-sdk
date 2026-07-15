from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared import CurrencyCode

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionCurrencyUpdated:
    action: SubscriptionHistoryAction
    currency_code: CurrencyCode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCurrencyUpdated:
        return SubscriptionHistoryDetailSubscriptionCurrencyUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            currency_code=CurrencyCode(data["currency_code"]),
        )
