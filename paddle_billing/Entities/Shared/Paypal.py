from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Paypal:
    email: str
    reference: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Paypal:
        return Paypal(
            email=data["email"],
            reference=data["reference"],
        )
