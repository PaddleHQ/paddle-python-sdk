from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.Interval import Interval


@dataclass
class Duration:
    interval: Interval
    frequency: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Duration:
        return Duration(
            interval=Interval(data["interval"]),
            frequency=data["frequency"],
        )
