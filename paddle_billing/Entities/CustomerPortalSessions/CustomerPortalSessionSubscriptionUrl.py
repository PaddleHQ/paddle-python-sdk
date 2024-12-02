from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CustomerPortalSessionSubscriptionUrl:
    id: str
    cancel_subscription: str
    update_subscription_payment_method: str

    @staticmethod
    def from_dict(data: dict) -> CustomerPortalSessionSubscriptionUrl:
        return CustomerPortalSessionSubscriptionUrl(
            id=data["id"],
            cancel_subscription=data["cancel_subscription"],
            update_subscription_payment_method=data["update_subscription_payment_method"],
        )
