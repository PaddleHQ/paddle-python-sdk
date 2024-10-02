from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TransactionCardType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AmericanExpress: "TransactionCardType" = "american_express"
    DinersClub: "TransactionCardType" = "diners_club"
    Discover: "TransactionCardType" = "discover"
    Jcb: "TransactionCardType" = "jcb"
    Mada: "TransactionCardType" = "mada"
    Maestro: "TransactionCardType" = "maestro"
    Mastercard: "TransactionCardType" = "mastercard"
    UnionPay: "TransactionCardType" = "union_pay"
    Unknown: "TransactionCardType" = "unknown"
    Visa: "TransactionCardType" = "visa"
