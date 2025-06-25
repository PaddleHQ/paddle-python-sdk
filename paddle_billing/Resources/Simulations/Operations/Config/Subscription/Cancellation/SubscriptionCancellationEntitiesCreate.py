from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionCancellationEntitiesCreate:
    subscription_id: str | None | Undefined = Undefined()
