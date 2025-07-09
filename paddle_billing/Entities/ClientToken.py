from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.ClientTokens import ClientTokenStatus


@dataclass
class ClientToken(Entity):
    id: str
    status: ClientTokenStatus
    token: str
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime
    revoked_at: datetime | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ClientToken:
        return ClientToken(
            id=data["id"],
            status=ClientTokenStatus(data["status"]),
            token=data["token"],
            name=data["name"],
            description=data.get("description"),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            revoked_at=datetime.fromisoformat(data["revoked_at"]) if data.get("revoked_at") else None,
        )
