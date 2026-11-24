from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SimulationKind(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Scenario: "SimulationKind" = member("scenario")
    SingleEvent: "SimulationKind" = member("single_event")
