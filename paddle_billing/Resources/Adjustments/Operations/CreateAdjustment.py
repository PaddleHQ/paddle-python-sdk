from dataclasses import dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Operation import Operation

from paddle_billing.Entities.Shared import Action, AdjustmentActionType

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustmentItem

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


@dataclass
class CreateAdjustment(Operation):
    action: Action
    items: list[CreateAdjustmentItem] | None | Undefined
    reason: str
    transaction_id: str
    type: AdjustmentActionType | Undefined = Undefined()

    def __post_init__(self):
        if self.type != AdjustmentActionType.Full and (
            self.items is None or isinstance(self.items, Undefined) or len(self.items) == 0
        ):
            raise InvalidArgumentException.array_is_empty("items")

        if self.type == AdjustmentActionType.Full and isinstance(self.items, list):
            raise InvalidArgumentException("items are not allowed when the adjustment type is full")

    @staticmethod
    def full(
        action: Action,
        reason: str,
        transaction_id: str,
    ) -> "CreateAdjustment":
        return CreateAdjustment(
            action=action,
            reason=reason,
            transaction_id=transaction_id,
            items=Undefined(),
            type=AdjustmentActionType.Full,
        )

    @staticmethod
    def partial(
        action: Action,
        items: list[CreateAdjustmentItem],
        reason: str,
        transaction_id: str,
    ) -> "CreateAdjustment":
        return CreateAdjustment(
            action=action,
            reason=reason,
            transaction_id=transaction_id,
            items=items,
            type=AdjustmentActionType.Partial,
        )
