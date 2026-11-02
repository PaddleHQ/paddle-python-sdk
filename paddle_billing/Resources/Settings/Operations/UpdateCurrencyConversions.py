from dataclasses import dataclass
from typing import Any

from paddle_billing.Operation import Operation
from paddle_billing.Entities.Settings import CurrencyConversionUpdate


@dataclass
class UpdateCurrencyConversions(Operation):
    """
    Send only the currencies you want to change, keyed by three-letter ISO 4217 currency code, for example `GBP`.
    Currencies you omit keep their current value.
    """

    conversions: dict[str, CurrencyConversionUpdate]

    def to_json(self) -> dict[str, Any]:
        return dict(self.conversions)
