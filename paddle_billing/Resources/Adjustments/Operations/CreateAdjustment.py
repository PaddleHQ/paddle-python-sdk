from dataclasses import dataclass

from paddle_billing.Entities.Shared import Action

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustmentItem


@dataclass
class CreateAdjustment:
    action:         Action
    items:          list[CreateAdjustmentItem]
    reason:         str
    transaction_id: str


    def get_parameters(self) -> dict:
        items = [{
            'item_id':  item.item_id,
            'type':     item.type,
            'amount':   item.amount,
        } for item in self.items]

        return {
            'action':         self.action.value,
            'items':          items,
            'reason':         self.reason,
            'transaction_id': self.transaction_id,
        }
