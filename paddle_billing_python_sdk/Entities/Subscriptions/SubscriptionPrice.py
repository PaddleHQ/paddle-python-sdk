from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.Money      import Money
from paddle_billing_python_sdk.Entities.Shared.TaxMode    import TaxMode
from paddle_billing_python_sdk.Entities.Shared.TimePeriod import TimePeriod


@dataclass
class SubscriptionPrice:
    id:            str
    description:   str
    product_id:    str
    billing_cycle: TimePeriod | None
    trial_period:  TimePeriod | None
    tax_mode:      TaxMode
    unit_price:    Money


    @staticmethod
    def from_dict(data: dict) -> SubscriptionPrice:
        return SubscriptionPrice(
            id            = data['id'],
            description   = data['description'],
            product_id    = data['product_id'],
            billing_cycle = TimePeriod.from_dict(data['billing_cycle']) if data.get('billing_cycle') else None,
            trial_period  = TimePeriod.from_dict(data['trial_period'])  if data.get('trial_period') else None,
            tax_mode      = TaxMode(data['tax_mode']),
            unit_price    = Money.from_dict(data['unit_price']),
        )
