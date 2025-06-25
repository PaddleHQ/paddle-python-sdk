from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.ApiKeys import ApiKeyPermission, ApiKeyStatus


@dataclass
class ApiKey(Entity):
    id: str
    name: str
    description: str | None
    key: str
    status: ApiKeyStatus
    permissions: list[ApiKeyPermission]
    expires_at: datetime | None
    last_used_at: datetime | None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKey:
        return ApiKey(
            id=data["id"],
            name=data["name"],
            description=data.get("description"),
            key=data["key"],
            status=ApiKeyStatus(data["status"]),
            permissions=[ApiKeyPermission(permission) for permission in data["permissions"]],
            expires_at=datetime.fromisoformat(data["expires_at"]) if data.get("expires_at") else None,
            last_used_at=datetime.fromisoformat(data["last_used_at"]) if data.get("last_used_at") else None,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
