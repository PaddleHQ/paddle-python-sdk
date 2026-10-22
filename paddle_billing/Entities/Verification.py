from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.VerificationStep import VerificationStep
from paddle_billing.Entities.Verifications import VerificationStatus, VerificationType


@dataclass
class Verification(Entity):
    id: str
    status: VerificationStatus
    verification_type: VerificationType
    steps: list[VerificationStep]
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Verification:
        return Verification(
            id=data["id"],
            status=VerificationStatus(data["status"]),
            verification_type=VerificationType(data["verification_type"]),
            steps=[VerificationStep.from_dict(step) for step in data["steps"]],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
