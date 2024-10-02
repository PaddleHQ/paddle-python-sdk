from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class AdjustmentCreditNote(Entity):
    url: str

    @staticmethod
    def from_dict(data: dict) -> AdjustmentCreditNote:
        return AdjustmentCreditNote(data["url"])
