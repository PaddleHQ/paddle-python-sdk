from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Transactions.TransactionTimePeriod import TransactionTimePeriod


@dataclass
class TransactionProration:
    rate:          str
    billingPeriod: TransactionTimePeriod | None


    @staticmethod
    def from_dict(data: dict) -> TransactionProration:
        return TransactionProration(
            rate          = data['rate'],
            billingPeriod = TransactionTimePeriod.from_dict(data['billing_period']) if 'billing_period' in data else None,
        )
