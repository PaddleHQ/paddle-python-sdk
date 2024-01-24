from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime


@dataclass
class AdjustmentTimePeriod:
    starts_at: datetime
    ends_at:   datetime


    @staticmethod
    def from_dict(data: dict) -> AdjustmentTimePeriod:
        return AdjustmentTimePeriod(
            starts_at = datetime.fromisoformat(data['starts_at']),
            ends_at   = datetime.fromisoformat(data['ends_at']),
        )
