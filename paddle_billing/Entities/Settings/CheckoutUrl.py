from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class CheckoutUrl(Entity):
    default_url: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CheckoutUrl:
        return CheckoutUrl(
            default_url=data["default_url"],
        )
