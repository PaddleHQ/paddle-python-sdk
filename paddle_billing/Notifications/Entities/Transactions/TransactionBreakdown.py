from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class TransactionBreakdown:
    credit: str
    refund: str
    chargeback: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionBreakdown:
        return TransactionBreakdown(
            credit=data["credit"],
            refund=data["refund"],
            chargeback=data["chargeback"],
        )
