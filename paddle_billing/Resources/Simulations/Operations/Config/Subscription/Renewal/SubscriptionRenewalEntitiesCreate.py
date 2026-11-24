from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class SubscriptionRenewalEntitiesCreate:
    subscription_id: str | None | Undefined = Undefined()
