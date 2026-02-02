from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.ApiKeyExposures import (
    ApiKeyExposureActionTaken,
    ApiKeyExposureRiskLevel,
    ApiKeyExposureSource,
)
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Undefined import Undefined


@dataclass
class ApiKeyExposure(SimulationEntity):
    id: str | Undefined = Undefined()
    api_key_id: str | Undefined = Undefined()
    risk_level: ApiKeyExposureRiskLevel | Undefined = Undefined()
    action_taken: ApiKeyExposureActionTaken | Undefined = Undefined()
    source: ApiKeyExposureSource | Undefined = Undefined()
    reference: str | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ApiKeyExposure:
        return ApiKeyExposure(
            id=data.get("id", Undefined()),
            api_key_id=data.get("api_key_id", Undefined()),
            risk_level=ApiKeyExposureRiskLevel(data["risk_level"]) if data.get("risk_level") else Undefined(),
            action_taken=ApiKeyExposureActionTaken(data["action_taken"]) if data.get("action_taken") else Undefined(),
            source=ApiKeyExposureSource(data["source"]) if data.get("source") else Undefined(),
            reference=data.get("reference", Undefined()),
            description=data.get("description", Undefined()),
            created_at=(
                datetime.fromisoformat(data["created_at"])
                if data.get("created_at")
                else data.get("created_at", Undefined())
            ),
        )
