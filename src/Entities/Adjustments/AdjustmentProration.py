from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Adjustments.AdjustmentTimePeriod import AdjustmentTimePeriod


@dataclass
class AdjustmentProration:
    rate:          str
    billingPeriod: AdjustmentTimePeriod


    @staticmethod
    def from_dict(data: dict) -> AdjustmentProration:
        return AdjustmentProration(
            rate          = data['rate'],
            billingPeriod = AdjustmentTimePeriod.from_dict(data['billing_period']),
        )
