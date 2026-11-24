from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ActionSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    System: "ActionSource" = member("system")
    Api: "ActionSource" = member("api")
    Dashboard: "ActionSource" = member("dashboard")
    CustomerPortal: "ActionSource" = member("customer_portal")
    SupportBot: "ActionSource" = member("support_bot")
    Retain: "ActionSource" = member("retain")
    Checkout: "ActionSource" = member("checkout")
    ExternalProvider: "ActionSource" = member("external_provider")
    PaddleClassic: "ActionSource" = member("paddle_classic")
    Unknown: "ActionSource" = member("unknown")
