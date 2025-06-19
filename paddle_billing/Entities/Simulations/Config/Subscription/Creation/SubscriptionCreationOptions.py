from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Simulations.Config.Options import (
    BusinessSimulatedAs,
    CustomerSimulatedAs,
    DiscountSimulatedAs,
)


@dataclass
class SubscriptionCreationOptions(Entity, ABC):
    customer_simulated_as: CustomerSimulatedAs
    business_simulated_as: BusinessSimulatedAs
    discount_simulated_as: DiscountSimulatedAs

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionCreationOptions:
        return SubscriptionCreationOptions(
            customer_simulated_as=CustomerSimulatedAs(data["customer_simulated_as"]),
            business_simulated_as=BusinessSimulatedAs(data["business_simulated_as"]),
            discount_simulated_as=DiscountSimulatedAs(data["discount_simulated_as"]),
        )
