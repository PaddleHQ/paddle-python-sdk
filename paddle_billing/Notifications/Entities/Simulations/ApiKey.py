from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.ApiKeys import ApiKeyPermission, ApiKeyStatus
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Undefined import Undefined


@dataclass
class ApiKey(SimulationEntity):
    id: str | Undefined = Undefined()
    name: str | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    key: str | Undefined = Undefined()
    status: ApiKeyStatus | Undefined = Undefined()
    permissions: list[ApiKeyPermission] | Undefined = Undefined()
    expires_at: datetime | None | Undefined = Undefined()
    last_used_at: datetime | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKey:
        return ApiKey(
            id=data.get("id", Undefined()),
            name=data.get("name", Undefined()),
            description=data.get("description", Undefined()),
            key=data.get("key", Undefined()),
            status=ApiKeyStatus(data["status"]) if data.get("status") else Undefined(),
            permissions=(
                [ApiKeyPermission(permission) for permission in data["permissions"]]
                if data.get("permissions")
                else Undefined()
            ),
            expires_at=(
                datetime.fromisoformat(data["expires_at"])
                if data.get("expires_at")
                else data.get("expires_at", Undefined())
            ),
            last_used_at=(
                datetime.fromisoformat(data["last_used_at"])
                if data.get("last_used_at")
                else data.get("last_used_at", Undefined())
            ),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
        )
