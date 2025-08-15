from pytest import raises

from paddle_billing.Resources.Events.Operations import ListEvents

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


class TestListEvents:
    def test_raises_invalid_argument_exception_for_invalid_event_types(self):
        with raises(InvalidArgumentException) as exception_info:
            ListEvents(event_types=["invalid.event"])

        assert str(exception_info.value) == "Expected 'event_types' to only contain type 'EventTypeName' ('str' given)"
