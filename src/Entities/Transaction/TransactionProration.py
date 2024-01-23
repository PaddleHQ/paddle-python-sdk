from __future__             import annotations
from .TransactionTimePeriod import TransactionTimePeriod
from dataclasses            import dataclass
from typing                 import Optional


@dataclass
class TransactionProration:
    rate:          str
    billingPeriod: Optional[TransactionTimePeriod]


    @staticmethod
    def from_dict(data: dict) -> TransactionProration:
        return TransactionProration(
            rate          = data['rate'],
            billingPeriod = TransactionTimePeriod.from_dict(data['billing_period']) if 'billing_period' in data else None,
        )
