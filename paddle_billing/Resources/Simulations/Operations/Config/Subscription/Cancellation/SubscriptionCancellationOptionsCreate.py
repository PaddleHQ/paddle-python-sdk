from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Simulations.Config.Options import EffectiveFrom
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionCancellationOptionsCreate:
    effective_from: EffectiveFrom | Undefined = Undefined()
    has_past_due_transaction: bool | Undefined = Undefined()
