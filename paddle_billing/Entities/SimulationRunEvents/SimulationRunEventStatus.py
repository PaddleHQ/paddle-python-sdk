from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SimulationRunEventStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Aborted: "SimulationRunEventStatus" = member("aborted")
    Failed: "SimulationRunEventStatus" = member("failed")
    Success: "SimulationRunEventStatus" = member("success")
    Pending: "SimulationRunEventStatus" = member("pending")
