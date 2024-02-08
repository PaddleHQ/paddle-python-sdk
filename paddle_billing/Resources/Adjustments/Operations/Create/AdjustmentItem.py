from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import AdjustmentType


@dataclass
class AdjustmentItem:
    item_id:   str
    type:      AdjustmentType
    amount:    str | None
