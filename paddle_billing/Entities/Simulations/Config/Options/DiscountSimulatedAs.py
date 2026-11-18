from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "DiscountSimulatedAs" = member("not_provided")
    Prefilled: "DiscountSimulatedAs" = member("prefilled")
    EnteredByCustomer: "DiscountSimulatedAs" = member("entered_by_customer")
