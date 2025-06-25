from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class PriceQuantity:
    minimum: int
    maximum: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PriceQuantity:
        return PriceQuantity(
            minimum=data["minimum"],
            maximum=data["maximum"],
        )
