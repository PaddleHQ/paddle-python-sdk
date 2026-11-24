from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class VerificationStepKey(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetup: "VerificationStepKey" = member("account_setup")
    DomainReview: "VerificationStepKey" = member("domain_review")
    BusinessIdentification: "VerificationStepKey" = member("business_identification")
    IdentityVerification: "VerificationStepKey" = member("identity_verification")
    FinalReview: "VerificationStepKey" = member("final_review")
    AutomatedReview: "VerificationStepKey" = member("automated_review")
