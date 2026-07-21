from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class SubscriptionHistoryItemUpdateSummary:
    quantity_delta: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryItemUpdateSummary:
        return SubscriptionHistoryItemUpdateSummary(
            quantity_delta=data["quantity_delta"],
        )
