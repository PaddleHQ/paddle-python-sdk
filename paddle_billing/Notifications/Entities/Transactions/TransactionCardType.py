from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class TransactionCardType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AmericanExpress: "TransactionCardType" = member("american_express")
    DinersClub: "TransactionCardType" = member("diners_club")
    Discover: "TransactionCardType" = member("discover")
    Jcb: "TransactionCardType" = member("jcb")
    Mada: "TransactionCardType" = member("mada")
    Maestro: "TransactionCardType" = member("maestro")
    Mastercard: "TransactionCardType" = member("mastercard")
    UnionPay: "TransactionCardType" = member("union_pay")
    Unknown: "TransactionCardType" = member("unknown")
    Visa: "TransactionCardType" = member("visa")
