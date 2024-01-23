from __future__                               import annotations
from dataclasses                              import dataclass
from .TransactionProration                    import TransactionProration
from src.Entities.Shared.AdjustmentItemTotals import AdjustmentItemTotals
from src.Entities.Shared.Type                 import Type
from typing                                   import Optional


@dataclass
class TransactionAdjustmentItem:
    id:        str
    itemId:    str
    type:      Type
    amount:    Optional[str]
    proration: TransactionProration
    totals:    AdjustmentItemTotals
