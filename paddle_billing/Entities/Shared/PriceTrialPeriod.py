from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.Duration import Duration
from paddle_billing.Entities.Shared.Interval import Interval
from paddle_billing.Entities.Shared.Money import Money
from paddle_billing.Entities.Shared.UnitPriceOverride import UnitPriceOverride
from paddle_billing.Undefined import Undefined


@dataclass
class PriceTrialPeriod(Duration):
    requires_payment_method: bool | Undefined = Undefined()
    unit_price: Money | None | Undefined = Undefined()
    unit_price_overrides: list[UnitPriceOverride] | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PriceTrialPeriod:
        return PriceTrialPeriod(
            interval=Interval(data["interval"]),
            frequency=data["frequency"],
            requires_payment_method=data.get("requires_payment_method", True),
            unit_price=Money.from_dict(data["unit_price"]) if data.get("unit_price") else None,
            unit_price_overrides=[
                UnitPriceOverride.from_dict(override) for override in data.get("unit_price_overrides", [])
            ],
        )
