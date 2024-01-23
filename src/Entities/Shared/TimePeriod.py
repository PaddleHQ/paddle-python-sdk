from __future__  import annotations
from .Interval   import Interval
from dataclasses import dataclass


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
