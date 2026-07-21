from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Shared.TimePeriod import TimePeriod

from paddle_billing.Notifications.Entities.Subscriptions.SubscriptionConsentRequirementType import (
    SubscriptionConsentRequirementType,
)
from paddle_billing.Notifications.Entities.Subscriptions.SubscriptionConsentRequirementStatus import (
    SubscriptionConsentRequirementStatus,
)


@dataclass
class SubscriptionConsentRequirement:
    id: str
    requirement: SubscriptionConsentRequirementType
    status: SubscriptionConsentRequirementStatus
    created_at: datetime
    consent_period: TimePeriod | None
    granted_at: datetime | None
    voided_at: datetime | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionConsentRequirement:
        return SubscriptionConsentRequirement(
            id=data["id"],
            requirement=SubscriptionConsentRequirementType(data["requirement"]),
            status=SubscriptionConsentRequirementStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            consent_period=TimePeriod.from_dict(data["consent_period"]) if data.get("consent_period") else None,
            granted_at=datetime.fromisoformat(data["granted_at"]) if data.get("granted_at") else None,
            voided_at=datetime.fromisoformat(data["voided_at"]) if data.get("voided_at") else None,
        )
