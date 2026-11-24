from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SimulationRunInclude(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Events: "SimulationRunInclude" = member("events")
