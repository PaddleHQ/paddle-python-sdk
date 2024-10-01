from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Action(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit: "Action" = "credit"
    CreditReverse: "Action" = "credit_reverse"
    Refund: "Action" = "refund"
    Chargeback: "Action" = "chargeback"
    ChargebackReverse: "Action" = "chargeback_reverse"
    ChargebackWarning: "Action" = "chargeback_warning"
