from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.CurrencyCodePayouts import CurrencyCodePayouts


@dataclass
class TransactionPayoutTotals:
    subtotal: str
    discount: str
    tax: str
    total: str
    credit: str
    balance: str
    grand_total: str
    fee: str | None
    earnings: str | None
    currency_code: CurrencyCodePayouts
    credit_to_balance: str
    exchange_rate: str
    fee_rate: str
    grand_total_tax: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionPayoutTotals:
        return TransactionPayoutTotals(
            subtotal=data["subtotal"],
            discount=data["discount"],
            tax=data["tax"],
            total=data["total"],
            credit=data["credit"],
            balance=data["balance"],
            grand_total=data["grand_total"],
            fee=data.get("fee"),
            earnings=data.get("earnings"),
            currency_code=CurrencyCodePayouts(data["currency_code"]),
            credit_to_balance=data["credit_to_balance"],
            exchange_rate=data["exchange_rate"],
            fee_rate=data["fee_rate"],
            grand_total_tax=data["grand_total_tax"],
        )
