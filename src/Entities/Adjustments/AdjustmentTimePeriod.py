from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime


@dataclass
class AdjustmentTimePeriod:
    startsAt: datetime
    endsAt:   datetime


    @staticmethod
    def from_dict(data: dict) -> AdjustmentTimePeriod:
        return AdjustmentTimePeriod(
            startsAt = datetime.fromisoformat(data['startsAt']),
            endsAt   = datetime.fromisoformat(data['endsAt']),
        )
