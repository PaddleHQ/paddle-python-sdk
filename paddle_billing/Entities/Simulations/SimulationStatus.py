from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SimulationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SimulationStatus" = member("active")
    Archived: "SimulationStatus" = member("archived")
