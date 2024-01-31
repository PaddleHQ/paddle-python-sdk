from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Shared.Action                 import Action
from paddle_billing.Entities.Shared.CurrencyCode           import CurrencyCode
from paddle_billing.Entities.Shared.PayoutTotalsAdjustment import PayoutTotalsAdjustment
from paddle_billing.Entities.Shared.StatusAdjustment       import StatusAdjustment
from paddle_billing.Entities.Shared.TotalAdjustments       import TotalAdjustments

from paddle_billing.Entities.Transactions.TransactionAdjustmentItem import TransactionAdjustmentItem


@dataclass
class TransactionAdjustment:
    id:                        str
    action:                    Action
    transaction_id:            str
    subscription_id:           str | None
    customer_id:               str
    reason:                    str
    credit_applied_to_balance: bool | None
    currency_code:             CurrencyCode
    status:                    StatusAdjustment
    items:                     list[TransactionAdjustmentItem]
    totals:                    TotalAdjustments
    payout_totals:             PayoutTotalsAdjustment | None
    created_at:                datetime
    updated_at:                datetime


    @staticmethod
    def from_dict(data: dict) -> TransactionAdjustment:
        return TransactionAdjustment(
            id                        = data['id'],
            action                    = Action(data['action']),
            transaction_id            = data['transaction_id'],
            subscription_id           = data.get('subscription_id'),
            customer_id               = data['customer_id'],
            reason                    = data['reason'],
            credit_applied_to_balance = data.get('credit_applied_to_balance'),
            currency_code             = CurrencyCode(data['currency_code']),
            status                    = StatusAdjustment(data['status']),
            items                     = [TransactionAdjustmentItem(item) for item in data['items']],
            totals                    = TotalAdjustments.from_dict(data['totals']),
            payout_totals             = PayoutTotalsAdjustment.from_dict(data['payout_totals']) if data.get('payout_totals') else None,
            created_at                = datetime.fromisoformat(data['created_at']),
            updated_at                = datetime.fromisoformat(data['updated_at']),
        )
