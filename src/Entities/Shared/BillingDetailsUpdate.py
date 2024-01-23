from __future__  import annotations
from .TimePeriod import TimePeriod
from dataclasses import dataclass


@dataclass
class BillingDetailsUpdate:
    enable_checkout:        bool
    purchase_order_number:  str
    additional_information: str
    payment_terms:          TimePeriod


    @staticmethod
    def from_dict(data: dict) -> BillingDetailsUpdate:
        return BillingDetailsUpdate(
            enable_checkout        = data['enable_checkout'],
            purchase_order_number  = data['purchase_order_number'],
            additional_information = data['additional_information'],
            payment_terms          = TimePeriod.from_dict(data['payment_terms']),
        )
