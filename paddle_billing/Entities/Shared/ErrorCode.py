from paddle_billing.PaddleStrEnum import PaddleStrEnum


class ErrorCode(PaddleStrEnum):
    AlreadyCanceled         = 'already_canceled'
    AlreadyRefunded         = 'already_refunded'
    AuthenticationFailed    = 'authentication_failed'
    BlockedCard             = 'blocked_card'
    Canceled                = 'canceled'
    Declined                = 'declined'
    ExpiredCard             = 'expired_card'
    Fraud                   = 'fraud'
    InvalidAmount           = 'invalid_amount'
    InvalidPaymentDetails   = 'invalid_payment_details'
    IssuerUnavailable       = 'issuer_unavailable'
    NotEnoughBalance        = 'not_enough_balance'
    PspError                = 'psp_error'
    RedactedPaymentMethod   = 'redacted_payment_method'
    SystemError             = 'system_error'
    TransactionNotPermitted = 'transaction_not_permitted'
    Unknown                 = 'unknown'
