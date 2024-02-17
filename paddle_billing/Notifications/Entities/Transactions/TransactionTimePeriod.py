from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime


@dataclass
class TransactionTimePeriod:
    starts_at: datetime
    ends_at:   datetime


    @staticmethod
    def from_dict(data: dict) -> TransactionTimePeriod:
        return TransactionTimePeriod(
            starts_at = datetime.fromisoformat(data['starts_at']),
            ends_at   = datetime.fromisoformat(data['ends_at']),
        )
