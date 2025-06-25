from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PaymentOutcome(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Success: "PaymentOutcome" = "success"
    RecoveredExistingPaymentMethod: "PaymentOutcome" = "recovered_existing_payment_method"
    RecoveredUpdatedPaymentMethod: "PaymentOutcome" = "recovered_updated_payment_method"
    Failed: "PaymentOutcome" = "failed"
