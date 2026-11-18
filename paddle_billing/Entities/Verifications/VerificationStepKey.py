from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class VerificationStepKey(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetup: "VerificationStepKey" = member("account_setup")
    DomainReview: "VerificationStepKey" = member("domain_review")
    BusinessIdentification: "VerificationStepKey" = member("business_identification")
    IdentityVerification: "VerificationStepKey" = member("identity_verification")
    FinalReview: "VerificationStepKey" = member("final_review")
    AutomatedReview: "VerificationStepKey" = member("automated_review")
