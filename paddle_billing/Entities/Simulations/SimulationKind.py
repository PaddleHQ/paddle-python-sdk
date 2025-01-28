from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SimulationKind(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Scenario: "SimulationKind" = "scenario"
    SingleEvent: "SimulationKind" = "single_event"
