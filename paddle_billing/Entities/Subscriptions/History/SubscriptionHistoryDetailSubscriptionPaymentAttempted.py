from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import (
    SubscriptionHistoryAction as SubscriptionHistoryAction,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryPaymentAttemptedOperation import (
    SubscriptionHistoryPaymentAttemptedOperation as SubscriptionHistoryPaymentAttemptedOperation,
)


@dataclass
class SubscriptionHistoryDetailSubscriptionPaymentAttempted:
    action: SubscriptionHistoryAction
    operation: SubscriptionHistoryPaymentAttemptedOperation
    transaction_id: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPaymentAttempted:
        return SubscriptionHistoryDetailSubscriptionPaymentAttempted(
            action=SubscriptionHistoryAction(data["action"]),
            operation=SubscriptionHistoryPaymentAttemptedOperation(data["operation"]),
            transaction_id=data["transaction_id"],
        )
