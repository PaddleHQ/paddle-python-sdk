from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SimulationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SimulationStatus" = member("active")
    Archived: "SimulationStatus" = member("archived")
