from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailItem import SubscriptionHistoryDetailItem
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryOneOffChargeAppliedEffectiveFrom import (
    SubscriptionHistoryOneOffChargeAppliedEffectiveFrom,
)
from paddle_billing.Entities.Subscriptions.SubscriptionOnPaymentFailure import SubscriptionOnPaymentFailure


@dataclass
class SubscriptionHistoryDetailSubscriptionOneOffChargeApplied:
    action: SubscriptionHistoryAction
    effective_from: SubscriptionHistoryOneOffChargeAppliedEffectiveFrom
    items: list[SubscriptionHistoryDetailItem]
    on_payment_failure: SubscriptionOnPaymentFailure
    transaction_id: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionOneOffChargeApplied:
        return SubscriptionHistoryDetailSubscriptionOneOffChargeApplied(
            action=SubscriptionHistoryAction(data["action"]),
            effective_from=SubscriptionHistoryOneOffChargeAppliedEffectiveFrom(data["effective_from"]),
            items=[SubscriptionHistoryDetailItem.from_dict(item) for item in data["items"]],
            on_payment_failure=SubscriptionOnPaymentFailure(data["on_payment_failure"]),
            transaction_id=data.get("transaction_id"),
        )
