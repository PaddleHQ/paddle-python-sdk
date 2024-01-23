from __future__  import annotations
from .TimePeriod import TimePeriod
from dataclasses import dataclass
from typing      import Optional


@dataclass
class BillingDetails:
    enable_checkout:        bool
    payment_terms:          TimePeriod
    purchase_order_number:  Optional[str] = None
    additional_information: Optional[str] = None


    @staticmethod
    def from_dict(data: dict) -> BillingDetails:
        return BillingDetails(
            enable_checkout        = data['enable_checkout'],
            payment_terms          = TimePeriod.from_dict(data['payment_terms']),
            purchase_order_number  = data.get('purchase_order_number'),
            additional_information = data.get('additional_information'),
        )
