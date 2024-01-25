from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.Action                 import Action
from paddle_billing_python_sdk.Entities.Shared.AdjustmentItemTotals   import AdjustmentItemTotals
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode           import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.PayoutTotalsAdjustment import PayoutTotalsAdjustment
from paddle_billing_python_sdk.Entities.Shared.StatusAdjustment       import StatusAdjustment
from paddle_billing_python_sdk.Entities.Shared.TotalAdjustments       import TotalAdjustments


@dataclass
class Adjustment(Entity):
    id:                        str
    action:                    Action
    transaction_id:            str
    subscription_id:           str | None
    customer_id:               str
    reason:                    str
    credit_applied_to_balance: bool | None
    currency_code:             CurrencyCode
    status:                    StatusAdjustment
    items:                     list[AdjustmentItemTotals]
    totals:                    TotalAdjustments
    payout_totals:             PayoutTotalsAdjustment | None
    created_at:                datetime
    updated_at:                datetime | None


    @classmethod
    def from_dict(cls, data: dict) -> Adjustment:
        return Adjustment(
            id                        = data['id'],
            action                    = Action(data['action']),
            transaction_id            = data['transaction_id'],
            subscription_id           = data.get('subscription_id'),
            customer_id               = data['customer_id'],
            reason                    = data['reason'],
            credit_applied_to_balance = data.get('credit_applied_to_balance'),
            currency_code             = CurrencyCode(data['currency_code']),
            status                    = StatusAdjustment(data['status']),
            items                     = [AdjustmentItemTotals.from_dict(item) for item in data['items']],
            totals                    = TotalAdjustments.from_dict(data['totals']),
            payout_totals             = PayoutTotalsAdjustment.from_dict(data['payout_totals']) if data.get('payout_totals') else None,
            created_at                = datetime.fromisoformat(data['created_at']),
            updated_at                = datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None,
        )
