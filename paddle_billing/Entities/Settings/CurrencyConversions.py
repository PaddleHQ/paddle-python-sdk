from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.CurrencyConversion import CurrencyConversion


@dataclass
class CurrencyConversions(Entity):
    """
    Currency conversion settings, keyed by three-letter ISO 4217 currency code, for example `USD`.
    """

    conversions: dict[str, CurrencyConversion]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CurrencyConversions:
        return CurrencyConversions(
            conversions={code: CurrencyConversion.from_dict(setting) for code, setting in data.items()},
        )
