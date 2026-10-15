from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class SubscriptionManagementUrls:
    update_payment_method: str | None
    cancel: str
    view_subscription: str | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionManagementUrls:
        return SubscriptionManagementUrls(
            update_payment_method=data.get("update_payment_method"),
            cancel=data["cancel"],
            view_subscription=data.get("view_subscription"),
        )
