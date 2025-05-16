from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.CustomerPortalSessions import CustomerPortalSessionUrls


@dataclass
class CustomerPortalSession(Entity):
    id: str
    customer_id: str
    urls: CustomerPortalSessionUrls
    created_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CustomerPortalSession:
        return CustomerPortalSession(
            id=data["id"],
            customer_id=data["customer_id"],
            urls=CustomerPortalSessionUrls.from_dict(data["urls"]),
            created_at=datetime.fromisoformat(data["created_at"]),
        )
