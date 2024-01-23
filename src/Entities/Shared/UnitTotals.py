from __future__  import annotations
from dataclasses import dataclass


@dataclass
class UnitTotals:
    subtotal: str
    discount: str
    tax:      str
    total:    str


    @staticmethod
    def from_dict(data: dict) -> UnitTotals:
        return UnitTotals(
            subtotal = data['subtotal'],
            discount = data['discount'],
            tax      = data['tax'],
            total    = data['total'],
        )
