from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.Interval import Interval


@dataclass
class TimePeriod:
    interval:  Interval
    frequency: int


    @staticmethod
    def from_dict(data: dict) -> TimePeriod:
        return TimePeriod(
            interval  = Interval(data['interval']),
            frequency = data['frequency'],
        )
