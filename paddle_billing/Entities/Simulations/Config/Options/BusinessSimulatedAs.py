from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class BusinessSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "BusinessSimulatedAs" = member("not_provided")
    New: "BusinessSimulatedAs" = member("new")
    ExistingDetailsPrefilled: "BusinessSimulatedAs" = member("existing_details_prefilled")
