from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.Interval import Interval


@dataclass
class Duration:
    interval: Interval
    frequency: int

    @staticmethod
    def from_dict(data: dict) -> Duration:
        return Duration(
            interval=Interval(data["interval"]),
            frequency=data["frequency"],
        )
