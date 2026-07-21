from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ActionSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    System: "ActionSource" = "system"
    Api: "ActionSource" = "api"
    Dashboard: "ActionSource" = "dashboard"
    CustomerPortal: "ActionSource" = "customer_portal"
    SupportBot: "ActionSource" = "support_bot"
    Retain: "ActionSource" = "retain"
    Checkout: "ActionSource" = "checkout"
    ExternalProvider: "ActionSource" = "external_provider"
    PaddleClassic: "ActionSource" = "paddle_classic"
    Unknown: "ActionSource" = "unknown"
