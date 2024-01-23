from __future__              import annotations
from .SubscriptionTimePeriod import SubscriptionTimePeriod
from dataclasses             import dataclass


@dataclass
class SubscriptionProration:
    rate:           str
    billing_period: SubscriptionTimePeriod


    @staticmethod
    def from_dict(data: dict) -> SubscriptionProration:
        return SubscriptionProration(
            rate           = data['rate'],
            billing_period = SubscriptionTimePeriod.from_dict(data['billing_period']),
        )
