from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class BusinessSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "BusinessSimulatedAs" = "not_provided"
    New: "BusinessSimulatedAs" = "new"
    ExistingDetailsPrefilled: "BusinessSimulatedAs" = "existing_details_prefilled"
