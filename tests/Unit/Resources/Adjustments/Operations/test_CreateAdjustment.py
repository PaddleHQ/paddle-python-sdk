from pytest import mark, raises

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import Action, AdjustmentActionType
from paddle_billing.Resources.Adjustments.Operations import CreateAdjustment
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


class TestCreateAdjustment:
    @mark.parametrize(
        "items",
        [
            (None),
            (Undefined()),
        ],
        ids=[
            "Full type with None items",
            "Full type with undefined items",
        ],
    )
    def test_does_not_raise_invalid_argument_exception_for_full_type_with_empty_items(
        self,
        items,
    ):
        operation = CreateAdjustment(
            Action.Refund, items, "error", "txn_01h8bxpvx398a7zbawb77y0kp5", AdjustmentActionType.Full
        )

        assert operation.items == items

    @mark.parametrize(
        "items, type, expected_message",
        [
            ([], AdjustmentActionType.Full, "items are not allowed when the adjustment type is full"),
            ([], AdjustmentActionType.Partial, "'items' cannot be empty"),
            ([], Undefined(), "'items' cannot be empty"),
        ],
        ids=[
            "Full type with items",
            "Partial type with empty items",
            "Undefined type with empty items",
        ],
    )
    def test_raises_invalid_argument_exception(self, items, type, expected_message):
        with raises(InvalidArgumentException) as exception_info:
            CreateAdjustment(Action.Refund, items, "error", "txn_01h8bxpvx398a7zbawb77y0kp5", type)

        assert str(exception_info.value) == expected_message
