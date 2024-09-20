from pytest import raises

from paddle_billing.Resources.Adjustments.Operations import ListAdjustments

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

class TestListAdjustments:
    def test_raises_invalid_argument_exception_for_invalid_ids(self):
        with raises(InvalidArgumentException) as exception_info:
            ListAdjustments(ids = [1])

        assert str(exception_info.value) == "Expected 'ids' to only contain only type/s 'str', '[1]' given"


    def test_raises_invalid_argument_exception_for_invalid_statuses(self):
        with raises(InvalidArgumentException) as exception_info:
            ListAdjustments(statuses = [1])

        assert str(exception_info.value) == "Expected 'statuses' to only contain only type/s 'AdjustmentStatus', '[1]' given"
