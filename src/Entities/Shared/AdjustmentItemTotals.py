from dataclasses import dataclass


@dataclass
class AdjustmentItemTotals:
    subtotal: str
    tax:      str
    total:    str
