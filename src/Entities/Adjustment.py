from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional, List

from src.Entities.Entity import Entity

from src.Entities.Shared.Action                 import Action
from src.Entities.Shared.AdjustmentItemTotals   import AdjustmentItemTotals
from src.Entities.Shared.CurrencyCode           import CurrencyCode
from src.Entities.Shared.PayoutTotalsAdjustment import PayoutTotalsAdjustment
from src.Entities.Shared.StatusAdjustment       import StatusAdjustment
from src.Entities.Shared.TotalAdjustments       import TotalAdjustments


@dataclass
class Adjustment(Entity):
    id:                     str
    action:                 Action
    transactionId:          str
    subscriptionId:         Optional[str]
    customerId:             str
    reason:                 str
    creditAppliedToBalance: Optional[bool]
    currencyCode:           CurrencyCode
    status:                 StatusAdjustment
    items:                  List[AdjustmentItemTotals]
    totals:                 TotalAdjustments
    payoutTotals:           Optional[PayoutTotalsAdjustment]
    createdAt:              datetime
    updatedAt:              Optional[datetime]


    @classmethod
    def from_dict(cls, data: dict) -> Adjustment:
        return Adjustment(
            id                     = data['id'],
            action                 = Action(data['action']),
            transactionId          = data['transaction_id'],
            subscriptionId         = data.get('subscription_id'),
            customerId             = data['customer_id'],
            reason                 = data['reason'],
            creditAppliedToBalance = data.get('credit_applied_to_balance'),
            currencyCode           = CurrencyCode(data['currency_code']),
            status                 = StatusAdjustment(data['status']),
            items                  = [AdjustmentItemTotals(item) for item in data['items']],
            totals                 = TotalAdjustments.from_dict(data['totals']),
            payoutTotals           = PayoutTotalsAdjustment.from_dict(data['payout_totals']) if 'payout_totals' in data else None,
            createdAt              = datetime.fromisoformat(data['created_at']),
            updatedAt              = datetime.fromisoformat(data['updated_at']) if 'updated_at' in data else None,
        )