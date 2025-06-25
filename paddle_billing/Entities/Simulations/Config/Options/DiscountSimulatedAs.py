from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "DiscountSimulatedAs" = "not_provided"
    Prefilled: "DiscountSimulatedAs" = "prefilled"
    EnteredByCustomer: "DiscountSimulatedAs" = "entered_by_customer"
