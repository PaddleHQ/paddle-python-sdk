from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class BalanceMovementType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Rebate: "BalanceMovementType" = "rebate"
    SwiftFee: "BalanceMovementType" = "swift_fee"
    Sale: "BalanceMovementType" = "sale"
    Refund: "BalanceMovementType" = "refund"
    ChargebackWarning: "BalanceMovementType" = "chargeback_warning"
    ChargebackWarningReverse: "BalanceMovementType" = "chargeback_warning_reverse"
    Chargeback: "BalanceMovementType" = "chargeback"
    ChargebackReverse: "BalanceMovementType" = "chargeback_reverse"
    Credit: "BalanceMovementType" = "credit"
