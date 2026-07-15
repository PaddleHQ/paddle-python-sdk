from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Price import Price

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryItemUpdateSummary import (
    SubscriptionHistoryItemUpdateSummary,
)
from paddle_billing.Entities.Subscriptions.SubscriptionOnPaymentFailure import SubscriptionOnPaymentFailure
from paddle_billing.Entities.Subscriptions.SubscriptionProrationBillingMode import SubscriptionProrationBillingMode


@dataclass
class SubscriptionHistoryDetailSubscriptionItemAdded:
    action: SubscriptionHistoryAction
    price: Price
    quantity: int
    update_summary: SubscriptionHistoryItemUpdateSummary
    proration_billing_mode: SubscriptionProrationBillingMode
    on_payment_failure: SubscriptionOnPaymentFailure
    transaction_id: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionItemAdded:
        return SubscriptionHistoryDetailSubscriptionItemAdded(
            action=SubscriptionHistoryAction(data["action"]),
            price=Price.from_dict(data["price"]),
            quantity=data["quantity"],
            update_summary=SubscriptionHistoryItemUpdateSummary.from_dict(data["update_summary"]),
            proration_billing_mode=SubscriptionProrationBillingMode(data["proration_billing_mode"]),
            on_payment_failure=SubscriptionOnPaymentFailure(data["on_payment_failure"]),
            transaction_id=data.get("transaction_id"),
        )
