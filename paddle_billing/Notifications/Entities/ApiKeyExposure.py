from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.ApiKeyExposures import (
    ApiKeyExposureActionTaken,
    ApiKeyExposureRiskLevel,
    ApiKeyExposureSource,
)


@dataclass
class ApiKeyExposure(Entity):
    id: str
    api_key_id: str
    risk_level: ApiKeyExposureRiskLevel
    action_taken: ApiKeyExposureActionTaken
    source: ApiKeyExposureSource
    reference: str
    description: str | None
    created_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKeyExposure:
        return ApiKeyExposure(
            id=data["id"],
            api_key_id=data["api_key_id"],
            risk_level=ApiKeyExposureRiskLevel(data["risk_level"]),
            action_taken=ApiKeyExposureActionTaken(data["action_taken"]),
            source=ApiKeyExposureSource(data["source"]),
            reference=data["reference"],
            description=data.get("description"),
            created_at=datetime.fromisoformat(data["created_at"]),
        )
