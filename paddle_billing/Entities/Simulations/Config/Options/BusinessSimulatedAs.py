from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class BusinessSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "BusinessSimulatedAs" = member("not_provided")
    New: "BusinessSimulatedAs" = member("new")
    ExistingDetailsPrefilled: "BusinessSimulatedAs" = member("existing_details_prefilled")
