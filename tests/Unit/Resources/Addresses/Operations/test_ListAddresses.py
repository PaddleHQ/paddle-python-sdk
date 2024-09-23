from pytest import raises

from paddle_billing.Resources.Addresses.Operations import ListAddresses

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

class TestListAddresses:
    def test_raises_invalid_argument_exception_for_invalid_ids(self):
        with raises(InvalidArgumentException) as exception_info:
            ListAddresses(ids = [1])

        assert str(exception_info.value) == "Expected 'ids' to only contain type 'string'"
