from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class TransactionPaypal:
    email: str
    reference: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionPaypal:
        return TransactionPaypal(
            email=data["email"],
            reference=data.get("reference"),
        )
