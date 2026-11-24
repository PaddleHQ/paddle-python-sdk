from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionConsentRequirementType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    TrialEnding: "SubscriptionConsentRequirementType" = member("trial_ending")
    IntroductoryDiscountEnding: "SubscriptionConsentRequirementType" = member("introductory_discount_ending")
