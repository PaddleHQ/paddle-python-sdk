from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ErrorCode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AlreadyCanceled: "ErrorCode" = member("already_canceled")
    AlreadyRefunded: "ErrorCode" = member("already_refunded")
    AuthenticationFailed: "ErrorCode" = member("authentication_failed")
    BlockedByPolicy: "ErrorCode" = member("blocked_by_policy")
    BlockedCard: "ErrorCode" = member("blocked_card")
    Canceled: "ErrorCode" = member("canceled")
    Declined: "ErrorCode" = member("declined")
    DeclinedNotRetryable: "ErrorCode" = member("declined_not_retryable")
    ExpiredCard: "ErrorCode" = member("expired_card")
    Fraud: "ErrorCode" = member("fraud")
    InvalidAmount: "ErrorCode" = member("invalid_amount")
    InvalidPaymentDetails: "ErrorCode" = member("invalid_payment_details")
    IssuerUnavailable: "ErrorCode" = member("issuer_unavailable")
    NotEnoughBalance: "ErrorCode" = member("not_enough_balance")
    PreferredNetworkNotSupported: "ErrorCode" = member("preferred_network_not_supported")
    PrepaidCardNotSupported: "ErrorCode" = member("prepaid_card_not_supported")
    PspError: "ErrorCode" = member("psp_error")
    RedactedPaymentMethod: "ErrorCode" = member("redacted_payment_method")
    SystemError: "ErrorCode" = member("system_error")
    TransactionNotPermitted: "ErrorCode" = member("transaction_not_permitted")
    Unknown: "ErrorCode" = member("unknown")
