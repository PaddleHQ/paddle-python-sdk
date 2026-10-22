from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricEntity(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    TransactionsCompleted: "MetricEntity" = "transactions.completed"
    AdjustmentsRefunds: "MetricEntity" = "adjustments.refunds"
    AdjustmentsChargebacks: "MetricEntity" = "adjustments.chargebacks"
    Checkouts: "MetricEntity" = "checkouts"
    Subscriptions: "MetricEntity" = "subscriptions"
