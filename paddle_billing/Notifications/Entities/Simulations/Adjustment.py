from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Adjustments import AdjustmentItem, AdjustmentTaxRatesUsed
from paddle_billing.Notifications.Entities.Shared import (
    Action,
    AdjustmentActionType,
    AdjustmentStatus,
    CurrencyCode,
    PayoutTotalsAdjustment,
    AdjustmentTotals,
)
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Adjustment(SimulationEntity):
    id: str | Undefined = Undefined()
    action: Action | Undefined = Undefined()
    transaction_id: str | Undefined = Undefined()
    subscription_id: str | None | Undefined = Undefined()
    customer_id: str | Undefined = Undefined()
    reason: str | Undefined = Undefined()
    credit_applied_to_balance: bool | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    status: AdjustmentStatus | Undefined = Undefined()
    items: list[AdjustmentItem] | Undefined = Undefined()
    totals: AdjustmentTotals | Undefined = Undefined()
    payout_totals: PayoutTotalsAdjustment | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | None | Undefined = Undefined()
    tax_rates_used: list[AdjustmentTaxRatesUsed] | None | Undefined = Undefined()
    type: AdjustmentActionType | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Adjustment:
        return Adjustment(
            id=data.get("id", Undefined()),
            action=Action(data["action"]) if data.get("action") else Undefined(),
            transaction_id=data.get("transaction_id", Undefined()),
            subscription_id=data.get("subscription_id", Undefined()),
            customer_id=data.get("customer_id", Undefined()),
            reason=data.get("reason", Undefined()),
            credit_applied_to_balance=data.get("credit_applied_to_balance", Undefined()),
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else Undefined(),
            status=AdjustmentStatus(data["status"]) if data.get("status") else Undefined(),
            totals=AdjustmentTotals.from_dict(data["totals"]) if data.get("totals") else Undefined(),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            items=[AdjustmentItem.from_dict(item) for item in data["items"]] if data.get("items") else Undefined(),
            payout_totals=(
                PayoutTotalsAdjustment.from_dict(data["payout_totals"])
                if data.get("payout_totals")
                else data.get("payout_totals", Undefined())
            ),
            updated_at=(
                datetime.fromisoformat(data["updated_at"])
                if data.get("updated_at")
                else data.get("updated_at", Undefined())
            ),
            tax_rates_used=(
                [AdjustmentTaxRatesUsed.from_dict(item) for item in data["tax_rates_used"]]
                if data.get("tax_rates_used")
                else data.get("tax_rates_used", Undefined())
            ),
            type=AdjustmentActionType(data["type"]) if data.get("type") else Undefined(),
        )
