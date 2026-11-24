from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountSimulatedAs(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotProvided: "DiscountSimulatedAs" = member("not_provided")
    Prefilled: "DiscountSimulatedAs" = member("prefilled")
    EnteredByCustomer: "DiscountSimulatedAs" = member("entered_by_customer")
