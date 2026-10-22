from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import ActionSource, Actor

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetail import (
    SubscriptionHistoryDetail,
    SubscriptionHistoryDetailUnion,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryReason import SubscriptionHistoryReason


@dataclass
class SubscriptionHistory(Entity):
    id: str
    group_id: str
    subscription_id: str
    occurred_at: datetime
    source: ActionSource
    actor: Actor
    reason: SubscriptionHistoryReason | None
    detail: SubscriptionHistoryDetailUnion

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistory:
        return SubscriptionHistory(
            id=data["id"],
            group_id=data["group_id"],
            subscription_id=data["subscription_id"],
            occurred_at=datetime.fromisoformat(data["occurred_at"]),
            source=ActionSource(data["source"]),
            actor=Actor.from_dict(data["actor"]),
            reason=SubscriptionHistoryReason(data["reason"]) if data.get("reason") else None,
            detail=SubscriptionHistoryDetail.from_dict(data["detail"]),
        )
