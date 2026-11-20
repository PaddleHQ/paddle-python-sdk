from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionHistoryReason(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    CardlessTrialEnded: "SubscriptionHistoryReason" = member("cardless_trial_ended")
    ImportIssue: "SubscriptionHistoryReason" = member("import_issue")
    MissingConsent: "SubscriptionHistoryReason" = member("missing_consent")
    SellerRequest: "SubscriptionHistoryReason" = member("seller_request")
    CustomerRequest: "SubscriptionHistoryReason" = member("customer_request")
    Chargeback: "SubscriptionHistoryReason" = member("chargeback")
    EuWithdrawal: "SubscriptionHistoryReason" = member("eu_withdrawal")
