from __future__  import annotations
from dataclasses import dataclass


@dataclass
class TransactionBreakdown:
    credit:     str
    refund:     str
    chargeback: str


    @staticmethod
    def from_dict(data: dict) -> TransactionBreakdown:
        return TransactionBreakdown(
            credit     = data['credit'],
            refund     = data['refund'],
            chargeback = data['chargeback'],
        )
