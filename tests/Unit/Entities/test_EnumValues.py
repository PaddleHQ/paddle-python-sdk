from pytest import mark

from paddle_billing.Entities.Shared import PaymentAttemptStatus
from paddle_billing.Notifications.Entities.Shared import (
    Action as NotificationAction,
    PaymentAttemptStatus as NotificationPaymentAttemptStatus,
)


class TestEnumValues:
    @mark.parametrize(
        "enum, value, expected_name",
        [
            (PaymentAttemptStatus, "dropped", "Dropped"),
            (NotificationPaymentAttemptStatus, "dropped", "Dropped"),
            (NotificationAction, "chargeback_warning_reverse", "ChargebackWarningReverse"),
        ],
        ids=[
            "PaymentAttemptStatus dropped",
            "Notification PaymentAttemptStatus dropped",
            "Notification Action chargeback_warning_reverse",
        ],
    )
    def test_value_is_known(self, enum, value, expected_name):
        member = enum(value)

        assert member.is_known()
        assert member.name == expected_name
        assert member == getattr(enum, expected_name)
