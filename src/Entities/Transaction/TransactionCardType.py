from enum import StrEnum


class TransactionCardType(StrEnum):
    AmericanExpress = 'american_express'
    DinersClub      = 'diners_club'
    Discover        = 'discover'
    Jcb             = 'jcb'
    Mada            = 'mada'
    Maestro         = 'maestro'
    Mastercard      = 'mastercard'
    UnionPay        = 'union_pay'
    Unknown         = 'unknown'
    Visa            = 'visa'
