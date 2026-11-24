from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SimulationScenarioType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionCreation: "SimulationScenarioType" = member("subscription_creation")
    SubscriptionRenewal: "SimulationScenarioType" = member("subscription_renewal")
    SubscriptionPause: "SimulationScenarioType" = member("subscription_pause")
    SubscriptionResume: "SimulationScenarioType" = member("subscription_resume")
    SubscriptionCancellation: "SimulationScenarioType" = member("subscription_cancellation")
