from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.ApiKeys import ApiKeyRotationStatus


@dataclass
class ApiKeyRotation(Entity):
    id: str
    api_key_id: str
    new_key: str
    grace_period_seconds: int
    new_key_expires_at: datetime | None
    expires_at: datetime | None
    status: ApiKeyRotationStatus
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKeyRotation:
        return ApiKeyRotation(
            id=data["id"],
            api_key_id=data["api_key_id"],
            new_key=data["new_key"],
            grace_period_seconds=data["grace_period_seconds"],
            new_key_expires_at=(
                datetime.fromisoformat(data["new_key_expires_at"]) if data.get("new_key_expires_at") else None
            ),
            expires_at=datetime.fromisoformat(data["expires_at"]) if data.get("expires_at") else None,
            status=ApiKeyRotationStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
