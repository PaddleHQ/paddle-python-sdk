from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.AdjustmentTimePeriod import AdjustmentTimePeriod


@dataclass
class AdjustmentProration:
    rate:           str
    billing_period: AdjustmentTimePeriod


    @staticmethod
    def from_dict(data: dict) -> AdjustmentProration:
        return AdjustmentProration(
            rate           = data['rate'],
            billing_period = AdjustmentTimePeriod.from_dict(data['billing_period']),
        )
