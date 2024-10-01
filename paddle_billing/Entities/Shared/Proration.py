from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.TimePeriod import TimePeriod


@dataclass
class Proration:
    rate: str
    billing_period: TimePeriod

    @staticmethod
    def from_dict(data: dict) -> Proration:
        return Proration(
            rate=data["rate"],
            billing_period=TimePeriod.from_dict(data["billing_period"]),
        )
