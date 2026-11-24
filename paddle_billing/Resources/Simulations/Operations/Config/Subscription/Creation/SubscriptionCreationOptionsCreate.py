from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Simulations.Config.Options import (
    BusinessSimulatedAs as BusinessSimulatedAs,
    CustomerSimulatedAs as CustomerSimulatedAs,
    DiscountSimulatedAs as DiscountSimulatedAs,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class SubscriptionCreationOptionsCreate:
    customer_simulated_as: CustomerSimulatedAs | Undefined = Undefined()
    business_simulated_as: BusinessSimulatedAs | Undefined = Undefined()
    discount_simulated_as: DiscountSimulatedAs | Undefined = Undefined()
