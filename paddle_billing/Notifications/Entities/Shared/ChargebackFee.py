from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.Original import Original


@dataclass
class ChargebackFee:
    amount:   str
    original: Original | None


    @staticmethod
    def from_dict(data: dict) -> ChargebackFee:
        return ChargebackFee(
            amount   = data['amount'],
            original = Original.from_dict(data['original']) if data.get('original') else None,
        )
