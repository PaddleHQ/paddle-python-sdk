from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Totals:
    subtotal: str
    discount: str
    tax: str
    total: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Totals:
        return Totals(
            subtotal=data["subtotal"],
            discount=data["discount"],
            tax=data["tax"],
            total=data["total"],
        )
