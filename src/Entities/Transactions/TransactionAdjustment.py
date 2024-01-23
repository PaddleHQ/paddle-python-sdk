from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Shared.Action                 import Action
from src.Entities.Shared.CurrencyCode           import CurrencyCode
from src.Entities.Shared.PayoutTotalsAdjustment import PayoutTotalsAdjustment
from src.Entities.Shared.StatusAdjustment       import StatusAdjustment
from src.Entities.Shared.TotalAdjustments       import TotalAdjustments

from src.Entities.Transactions.TransactionAdjustmentItem import TransactionAdjustmentItem


@dataclass
class TransactionAdjustment:
    id:                     str
    action:                 Action
    transactionId:          str
    subscriptionId:         str | None
    customerId:             str
    reason:                 str
    creditAppliedToBalance: bool | None
    currencyCode:           CurrencyCode
    status:                 StatusAdjustment
    items:                  list[TransactionAdjustmentItem]
    totals:                 TotalAdjustments
    payoutTotals:           PayoutTotalsAdjustment | None
    createdAt:              datetime
    updatedAt:              datetime


    @classmethod
    def from_dict(cls, data: dict) -> TransactionAdjustment:
        return TransactionAdjustment(
            id                     = data['id'],
            action                 = Action(data['action']),
            transactionId          = data['transaction_id'],
            subscriptionId         = data.get('subscription_id'),
            customerId             = data['customer_id'],
            reason                 = data['reason'],
            creditAppliedToBalance = data.get('credit_applied_to_balance'),
            currencyCode           = CurrencyCode(data['currency_code']),
            status                 = StatusAdjustment(data['status']),
            items                  = [TransactionAdjustmentItem(item) for item in data['items']],
            totals                 = TotalAdjustments.from_dict(data['totals']),
            payoutTotals           = PayoutTotalsAdjustment.from_dict(data['payout_totals']) if 'payout_totals' in data else None,
            createdAt              = datetime.fromisoformat(data['created_at']),
            updatedAt              = datetime.fromisoformat(data['updated_at']),
        )
