from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.CustomerPortalSessions.CustomerPortalSessionGeneralUrl import (
    CustomerPortalSessionGeneralUrl,
)
from paddle_billing.Entities.CustomerPortalSessions.CustomerPortalSessionSubscriptionUrl import (
    CustomerPortalSessionSubscriptionUrl,
)


@dataclass
class CustomerPortalSessionUrls:
    general: CustomerPortalSessionGeneralUrl
    subscriptions: list[CustomerPortalSessionSubscriptionUrl]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CustomerPortalSessionUrls:
        return CustomerPortalSessionUrls(
            general=CustomerPortalSessionGeneralUrl.from_dict(data["general"]),
            subscriptions=[
                CustomerPortalSessionSubscriptionUrl.from_dict(item) for item in data.get("subscriptions", [])
            ],
        )
