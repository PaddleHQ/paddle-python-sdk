from dataclasses import dataclass

from paddle_billing.Entities.Adjustments.AdjustmentItem import AdjustmentItem
from paddle_billing.Entities.Shared.Action              import Action


@dataclass
class CreateAdjustment:
    action:         Action
    items:          list[AdjustmentItem]
    reason:         str
    transaction_id: str


    def get_parameters(self) -> dict:
        items = [
            {
                'item_id': item.item_id,
                'type':    item.type.value,
                'amount':  item.amount,
            }
            for item in self.items
        ]

        return {
            'action':         self.action.value,
            'items':          items,
            'reason':         self.reason,
            'transaction_id': self.transaction_id,
        }
