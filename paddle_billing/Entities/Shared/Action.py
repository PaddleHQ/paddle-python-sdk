from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Action(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit: "Action" = member("credit")
    CreditReverse: "Action" = member("credit_reverse")
    Refund: "Action" = member("refund")
    Chargeback: "Action" = member("chargeback")
    ChargebackReverse: "Action" = member("chargeback_reverse")
    ChargebackWarning: "Action" = member("chargeback_warning")
    ChargebackWarningReverse: "Action" = member("chargeback_warning_reverse")
