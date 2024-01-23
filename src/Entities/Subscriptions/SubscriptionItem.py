from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional

from src.Entities.Subscriptions.SubscriptionItemStatus import SubscriptionItemStatus
from src.Entities.Subscriptions.SubscriptionPrice      import SubscriptionPrice
from src.Entities.Subscriptions.SubscriptionTimePeriod import SubscriptionTimePeriod


@dataclass
class SubscriptionItem:
    status:             SubscriptionItemStatus
    quantity:           int
    recurring:          bool
    createdAt:          datetime
    updatedAt:          datetime
    previouslyBilledAt: Optional[datetime]
    nextBilledAt:       Optional[datetime]
    trialDates:         Optional[SubscriptionTimePeriod]
    price:              SubscriptionPrice


    @staticmethod
    def from_dict(data: dict) -> SubscriptionItem:
        return SubscriptionItem(
            status             = SubscriptionItemStatus(data['status']),
            quantity           = data['quantity'],
            recurring          = data['recurring'],
            createdAt          = datetime.fromisoformat(data['created_at']),
            updatedAt          = datetime.fromisoformat(data['updated_at']),
            previouslyBilledAt = datetime.fromisoformat(data['previously_billed_at'])  if 'previously_billed_at' in data else None,
            nextBilledAt       = datetime.fromisoformat(data['next_billed_at'])        if 'next_billed_at'       in data else None,
            trialDates         = SubscriptionTimePeriod.from_dict(data['trial_dates']) if 'trial_dates'          in data else None,
            price              = SubscriptionPrice.from_dict(data['price']),
        )
