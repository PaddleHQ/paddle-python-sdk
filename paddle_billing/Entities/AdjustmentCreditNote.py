from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class AdjustmentCreditNote(Entity):
    url: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AdjustmentCreditNote:
        return AdjustmentCreditNote(data["url"])
