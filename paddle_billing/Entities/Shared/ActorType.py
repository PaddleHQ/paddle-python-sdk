from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ActorType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Customer: "ActorType" = member("customer")
    User: "ActorType" = member("user")
    ApiKey: "ActorType" = member("api_key")
    PaddleStaff: "ActorType" = member("paddle_staff")
    Publisher: "ActorType" = member("publisher")
    System: "ActorType" = member("system")
