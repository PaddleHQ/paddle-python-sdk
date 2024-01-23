from __future__                                 import annotations
from .TransactionAdjustmentItem                 import TransactionAdjustmentItem
from dataclasses                                import dataclass
from datetime                                   import datetime
from src.Entities.Shared.Action                 import Action
from src.Entities.Shared.CurrencyCode           import CurrencyCode
from src.Entities.Shared.StatusAdjustment       import StatusAdjustment
from src.Entities.Shared.TotalAdjustments       import TotalAdjustments
from src.Entities.Shared.PayoutTotalsAdjustment import PayoutTotalsAdjustment
from typing                                     import Optional, List


@dataclass
class TransactionAdjustment:
    id:                     str
    action:                 Action
    transactionId:          str
    subscriptionId:         Optional[str]
    customerId:             str
    reason:                 str
    creditAppliedToBalance: Optional[bool]
    currencyCode:           CurrencyCode
    status:                 StatusAdjustment
    items:                  List[TransactionAdjustmentItem]
    totals:                 TotalAdjustments
    payoutTotals:           Optional[PayoutTotalsAdjustment]
    createdAt:              datetime
    updatedAt:              datetime


    @classmethod
    def from_dict(cls, data: dict) -> TransactionAdjustment:
        return cls(
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
