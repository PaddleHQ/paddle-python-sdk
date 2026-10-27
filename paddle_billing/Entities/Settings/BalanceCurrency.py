from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.BalanceCurrencyCode import BalanceCurrencyCode


@dataclass
class BalanceCurrency(Entity):
    primary: BalanceCurrencyCode
    preferred: BalanceCurrencyCode
    enabled: list[BalanceCurrencyCode]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> BalanceCurrency:
        return BalanceCurrency(
            primary=BalanceCurrencyCode(data["primary"]),
            preferred=BalanceCurrencyCode(data["preferred"]),
            enabled=[BalanceCurrencyCode(currency) for currency in data["enabled"]],
        )
