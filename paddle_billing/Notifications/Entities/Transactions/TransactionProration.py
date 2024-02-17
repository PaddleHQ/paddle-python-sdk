from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Transactions.TransactionTimePeriod import TransactionTimePeriod


@dataclass
class TransactionProration:
    rate:           str
    billing_period: TransactionTimePeriod | None


    @staticmethod
    def from_dict(data: dict) -> TransactionProration:
        return TransactionProration(
            rate           = data['rate'],
            billing_period = TransactionTimePeriod.from_dict(data['billing_period']) if data.get('billing_period') else None,
        )
