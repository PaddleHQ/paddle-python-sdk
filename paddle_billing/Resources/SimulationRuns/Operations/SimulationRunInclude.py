from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SimulationRunInclude(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Events: "SimulationRunInclude" = member("events")
