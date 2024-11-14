from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity


@dataclass
class CustomerAuthToken(Entity):
    customer_auth_token: str
    expires_at: datetime

    @staticmethod
    def from_dict(data: dict) -> CustomerAuthToken:
        return CustomerAuthToken(
            customer_auth_token=data["customer_auth_token"],
            expires_at=datetime.fromisoformat(data["expires_at"]),
        )
