from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class PaymentOutcome(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Success: "PaymentOutcome" = member("success")
    RecoveredExistingPaymentMethod: "PaymentOutcome" = member("recovered_existing_payment_method")
    RecoveredUpdatedPaymentMethod: "PaymentOutcome" = member("recovered_updated_payment_method")
    Failed: "PaymentOutcome" = member("failed")
