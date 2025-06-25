from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SimulationScenarioType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionCreation: "SimulationScenarioType" = "subscription_creation"
    SubscriptionRenewal: "SimulationScenarioType" = "subscription_renewal"
    SubscriptionPause: "SimulationScenarioType" = "subscription_pause"
    SubscriptionResume: "SimulationScenarioType" = "subscription_resume"
    SubscriptionCancellation: "SimulationScenarioType" = "subscription_cancellation"
