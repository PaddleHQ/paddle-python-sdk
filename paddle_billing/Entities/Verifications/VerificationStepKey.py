from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class VerificationStepKey(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetup: "VerificationStepKey" = "account_setup"
    DomainReview: "VerificationStepKey" = "domain_review"
    BusinessIdentification: "VerificationStepKey" = "business_identification"
    IdentityVerification: "VerificationStepKey" = "identity_verification"
    FinalReview: "VerificationStepKey" = "final_review"
    AutomatedReview: "VerificationStepKey" = "automated_review"
