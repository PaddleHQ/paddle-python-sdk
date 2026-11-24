from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricEntity(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    TransactionsCompleted: "MetricEntity" = member("transactions.completed")
    AdjustmentsRefunds: "MetricEntity" = member("adjustments.refunds")
    AdjustmentsChargebacks: "MetricEntity" = member("adjustments.chargebacks")
    Checkouts: "MetricEntity" = member("checkouts")
    Subscriptions: "MetricEntity" = member("subscriptions")
