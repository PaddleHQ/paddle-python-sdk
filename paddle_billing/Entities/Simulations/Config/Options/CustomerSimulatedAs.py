from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CustomerSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    New: "CustomerSimulatedAs" = member("new")
    ExistingEmailMatched: "CustomerSimulatedAs" = member("existing_email_matched")
    ExistingDetailsPrefilled: "CustomerSimulatedAs" = member("existing_details_prefilled")
