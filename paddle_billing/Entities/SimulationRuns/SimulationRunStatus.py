from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SimulationRunStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Canceled: "SimulationRunStatus" = member("canceled")
    Completed: "SimulationRunStatus" = member("completed")
    Pending: "SimulationRunStatus" = member("pending")
