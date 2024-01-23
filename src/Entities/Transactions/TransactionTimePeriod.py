from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime


@dataclass
class TransactionTimePeriod:
    startsAt: datetime
    endsAt:   datetime


    @staticmethod
    def from_dict(data: dict) -> TransactionTimePeriod:
        return TransactionTimePeriod(
            startsAt = datetime.fromisoformat(data['starts_at']),
            endsAt   = datetime.fromisoformat(data['ends_at']),
        )
