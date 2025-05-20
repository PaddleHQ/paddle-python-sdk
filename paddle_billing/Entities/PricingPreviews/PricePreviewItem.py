from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class PricePreviewItem:
    price_id: str
    quantity: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PricePreviewItem:
        return PricePreviewItem(
            price_id=data["price_id"],
            quantity=data["quantity"],
        )
