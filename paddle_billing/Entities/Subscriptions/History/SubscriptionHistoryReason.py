from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionHistoryReason(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    CardlessTrialEnded: "SubscriptionHistoryReason" = "cardless_trial_ended"
    ImportIssue: "SubscriptionHistoryReason" = "import_issue"
    MissingConsent: "SubscriptionHistoryReason" = "missing_consent"
    SellerRequest: "SubscriptionHistoryReason" = "seller_request"
    CustomerRequest: "SubscriptionHistoryReason" = "customer_request"
    Chargeback: "SubscriptionHistoryReason" = "chargeback"
