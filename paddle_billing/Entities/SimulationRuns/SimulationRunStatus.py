from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SimulationRunStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Canceled: "SimulationRunStatus" = "canceled"
    Completed: "SimulationRunStatus" = "completed"
    Pending: "SimulationRunStatus" = "pending"
