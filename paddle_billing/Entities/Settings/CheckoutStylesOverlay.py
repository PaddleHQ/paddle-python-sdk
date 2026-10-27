from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class CheckoutStylesOverlay(Entity):
    primary_checkout_color: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutStylesOverlay:
        return CheckoutStylesOverlay(
            primary_checkout_color=data["primary_checkout_color"],
        )
