from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class AdjustmentCustomerBalance:
    available: str
    reserved: str
    used: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AdjustmentCustomerBalance:
        return AdjustmentCustomerBalance(
            available=data["available"],
            reserved=data["reserved"],
            used=data["used"],
        )
