from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionConsentRequirement import SubscriptionConsentRequirement


@dataclass
class SubscriptionHistoryDetailSubscriptionConsentRequirementGranted:
    action: SubscriptionHistoryAction
    consent_requirement: SubscriptionConsentRequirement

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionConsentRequirementGranted:
        return SubscriptionHistoryDetailSubscriptionConsentRequirementGranted(
            action=SubscriptionHistoryAction(data["action"]),
            consent_requirement=SubscriptionConsentRequirement.from_dict(data["consent_requirement"]),
        )
