from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SimulationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SimulationStatus" = "active"
    Archived: "SimulationStatus" = "archived"
