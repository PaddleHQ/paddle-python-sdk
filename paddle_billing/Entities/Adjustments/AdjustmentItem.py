from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import AdjustmentItemTotals, AdjustmentType, Proration


@dataclass
class AdjustmentItem:
    id: str
    item_id: str
    type: AdjustmentType
    amount: str | None
    proration: Proration | None
    totals: AdjustmentItemTotals

    @staticmethod
    def from_dict(data: dict) -> AdjustmentItem:
        return AdjustmentItem(
            id=data["id"],
            item_id=data["item_id"],
            type=AdjustmentType(data["type"]),
            amount=data.get("amount"),
            proration=Proration.from_dict(data["proration"]) if data.get("proration") else None,
            totals=AdjustmentItemTotals.from_dict(data["totals"]),
        )
