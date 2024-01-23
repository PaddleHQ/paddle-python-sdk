from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.Money      import Money
from src.Entities.Shared.TaxMode    import TaxMode
from src.Entities.Shared.TimePeriod import TimePeriod


@dataclass
class SubscriptionPrice:
    id:           str
    description:  str
    productId:    str
    billingCycle: TimePeriod | None
    trialPeriod:  TimePeriod | None
    taxMode:      TaxMode
    unitPrice:    Money


    @staticmethod
    def from_dict(data: dict) -> SubscriptionPrice:
        return SubscriptionPrice(
            id          = data['id'],
            description = data['description'],
            productId   = data['product_id'],
            billingCycle= TimePeriod.from_dict(data['billing_cycle']) if 'billing_cycle' in data else None,
            trialPeriod = TimePeriod.from_dict(data['trial_period'])  if 'trial_period'  in data else None,
            taxMode     = TaxMode(data['tax_mode']),
            unitPrice   = Money.from_dict(data['unit_price']),
        )
