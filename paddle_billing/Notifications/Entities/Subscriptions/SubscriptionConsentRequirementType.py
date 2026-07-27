from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionConsentRequirementType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    TrialEnding: "SubscriptionConsentRequirementType" = "trial_ending"
    IntroductoryDiscountEnding: "SubscriptionConsentRequirementType" = "introductory_discount_ending"
