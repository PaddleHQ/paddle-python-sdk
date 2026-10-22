from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionOnResume import SubscriptionOnResume
from paddle_billing.Entities.Subscriptions.SubscriptionStatus import SubscriptionStatus


@dataclass
class SubscriptionHistoryDetailSubscriptionResumed:
    action: SubscriptionHistoryAction
    status: SubscriptionStatus
    on_resume: SubscriptionOnResume

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionResumed:
        return SubscriptionHistoryDetailSubscriptionResumed(
            action=SubscriptionHistoryAction(data["action"]),
            status=SubscriptionStatus(data["status"]),
            on_resume=SubscriptionOnResume(data["on_resume"]),
        )
