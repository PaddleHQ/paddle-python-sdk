from paddle_billing.Entities.Notifications import NotificationPayout, NotificationPayoutStatus
from paddle_billing.Entities.Shared import CurrencyCodePayouts


def test_notification_payout_from_dict():
    payout = NotificationPayout.from_dict({"id": "pay_1", "status": "paid", "amount": "100", "currency_code": "USD"})

    assert payout.id == "pay_1"
    assert payout.status == NotificationPayoutStatus.Paid
    assert payout.amount == "100"
    assert payout.currency_code == CurrencyCodePayouts.USD
