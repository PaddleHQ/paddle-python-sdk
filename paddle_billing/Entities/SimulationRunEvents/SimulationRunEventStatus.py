from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SimulationRunEventStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Aborted: "SimulationRunEventStatus" = "aborted"
    Failed: "SimulationRunEventStatus" = "failed"
    Success: "SimulationRunEventStatus" = "success"
    Pending: "SimulationRunEventStatus" = "pending"
