from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Creation.SubscriptionCreationItemCreate import (
    SubscriptionCreationItemCreate,
)
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionCreationEntitiesCreate:
    customer_id: str | None | Undefined = Undefined()
    address_id: str | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    payment_method_id: str | None | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    transaction_id: str | None | Undefined = Undefined()
    items: list[SubscriptionCreationItemCreate] | None | Undefined = Undefined()

    def __post_init__(self):
        if isinstance(self.transaction_id, str) and isinstance(self.items, list):
            raise InvalidArgumentException.incompatible_arguments("transaction_id", "items")
