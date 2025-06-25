from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CustomerSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    New: "CustomerSimulatedAs" = "new"
    ExistingEmailMatched: "CustomerSimulatedAs" = "existing_email_matched"
    ExistingDetailsPrefilled: "CustomerSimulatedAs" = "existing_details_prefilled"
