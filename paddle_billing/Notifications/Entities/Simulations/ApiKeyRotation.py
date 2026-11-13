from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.ApiKeys import ApiKeyRotationStatus
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Undefined import Undefined


@dataclass
class ApiKeyRotation(SimulationEntity):
    id: str | Undefined = Undefined()
    api_key_id: str | Undefined = Undefined()
    status: ApiKeyRotationStatus | Undefined = Undefined()
    grace_period_seconds: int | Undefined = Undefined()
    new_key_expires_at: datetime | None | Undefined = Undefined()
    expires_at: datetime | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKeyRotation:
        return ApiKeyRotation(
            id=data.get("id", Undefined()),
            api_key_id=data.get("api_key_id", Undefined()),
            status=ApiKeyRotationStatus(data["status"]) if data.get("status") else Undefined(),
            grace_period_seconds=data.get("grace_period_seconds", Undefined()),
            new_key_expires_at=(
                datetime.fromisoformat(data["new_key_expires_at"])
                if data.get("new_key_expires_at")
                else data.get("new_key_expires_at", Undefined())
            ),
            expires_at=(
                datetime.fromisoformat(data["expires_at"])
                if data.get("expires_at")
                else data.get("expires_at", Undefined())
            ),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
        )
