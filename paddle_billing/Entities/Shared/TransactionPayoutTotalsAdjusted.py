from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.ChargebackFee import ChargebackFee
from paddle_billing.Entities.Shared.CurrencyCodePayouts import CurrencyCodePayouts


@dataclass
class TransactionPayoutTotalsAdjusted:
    subtotal: str
    tax: str
    total: str
    fee: str
    chargeback_fee: ChargebackFee
    earnings: str
    currency_code: CurrencyCodePayouts
    exchange_rate: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionPayoutTotalsAdjusted:
        return TransactionPayoutTotalsAdjusted(
            subtotal=data["subtotal"],
            tax=data["tax"],
            total=data["total"],
            fee=data["fee"],
            chargeback_fee=ChargebackFee.from_dict(data["chargeback_fee"]),
            earnings=data["earnings"],
            currency_code=CurrencyCodePayouts(data["currency_code"]),
            exchange_rate=data["exchange_rate"],
        )
