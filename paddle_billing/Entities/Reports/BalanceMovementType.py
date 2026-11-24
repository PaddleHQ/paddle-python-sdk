from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class BalanceMovementType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Rebate: "BalanceMovementType" = member("rebate")
    SwiftFee: "BalanceMovementType" = member("swift_fee")
    Sale: "BalanceMovementType" = member("sale")
    Refund: "BalanceMovementType" = member("refund")
    ChargebackWarning: "BalanceMovementType" = member("chargeback_warning")
    ChargebackWarningReverse: "BalanceMovementType" = member("chargeback_warning_reverse")
    Chargeback: "BalanceMovementType" = member("chargeback")
    ChargebackReverse: "BalanceMovementType" = member("chargeback_reverse")
    Credit: "BalanceMovementType" = member("credit")
