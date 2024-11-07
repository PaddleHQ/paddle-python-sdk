from dataclasses import dataclass

from paddle_billing.Operation import Operation

from paddle_billing.Entities.Shared import Action

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustmentItem


@dataclass
class CreateAdjustment(Operation):
    action: Action
    items: list[CreateAdjustmentItem]
    reason: str
    transaction_id: str
