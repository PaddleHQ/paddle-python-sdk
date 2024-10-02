from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ErrorCode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AlreadyCanceled: "ErrorCode" = "already_canceled"
    AlreadyRefunded: "ErrorCode" = "already_refunded"
    AuthenticationFailed: "ErrorCode" = "authentication_failed"
    BlockedCard: "ErrorCode" = "blocked_card"
    Canceled: "ErrorCode" = "canceled"
    Declined: "ErrorCode" = "declined"
    ExpiredCard: "ErrorCode" = "expired_card"
    Fraud: "ErrorCode" = "fraud"
    InvalidAmount: "ErrorCode" = "invalid_amount"
    InvalidPaymentDetails: "ErrorCode" = "invalid_payment_details"
    IssuerUnavailable: "ErrorCode" = "issuer_unavailable"
    NotEnoughBalance: "ErrorCode" = "not_enough_balance"
    PspError: "ErrorCode" = "psp_error"
    RedactedPaymentMethod: "ErrorCode" = "redacted_payment_method"
    SystemError: "ErrorCode" = "system_error"
    TransactionNotPermitted: "ErrorCode" = "transaction_not_permitted"
    Unknown: "ErrorCode" = "unknown"
