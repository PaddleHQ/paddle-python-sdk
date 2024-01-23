from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional

from src.Entities.Shared.AdjustmentItemTotals import AdjustmentItemTotals
from src.Entities.Shared.Type                 import Type

from src.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionAdjustmentItem:
    id:        str
    itemId:    str
    type:      Type
    amount:    Optional[str]
    proration: TransactionProration
    totals:    AdjustmentItemTotals
