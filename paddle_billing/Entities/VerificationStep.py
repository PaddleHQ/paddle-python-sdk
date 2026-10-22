from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Verifications import VerificationStepKey, VerificationStepStatus


@dataclass
class VerificationStep(Entity):
    id: str
    key: VerificationStepKey
    status: VerificationStepStatus
    expires_at: datetime | None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> VerificationStep:
        return VerificationStep(
            id=data["id"],
            key=VerificationStepKey(data["key"]),
            status=VerificationStepStatus(data["status"]),
            expires_at=datetime.fromisoformat(data["expires_at"]) if data.get("expires_at") else None,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
