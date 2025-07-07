from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Notifications.Entities.ClientTokens import ClientTokenStatus
from paddle_billing.Undefined import Undefined


@dataclass
class ClientToken(SimulationEntity):
    id: str | Undefined = Undefined()
    status: ClientTokenStatus | Undefined = Undefined()
    token: str | Undefined = Undefined()
    name: str | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    revoked_at: datetime | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ClientToken:
        return ClientToken(
            id=data.get("id", Undefined()),
            status=ClientTokenStatus(data["status"]) if data.get("status") else Undefined(),
            token=data.get("token", Undefined()),
            name=data.get("name", Undefined()),
            description=data.get("description", Undefined()),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            revoked_at=(
                datetime.fromisoformat(data["revoked_at"])
                if data.get("revoked_at")
                else data.get("revoked_at", Undefined())
            ),
        )
