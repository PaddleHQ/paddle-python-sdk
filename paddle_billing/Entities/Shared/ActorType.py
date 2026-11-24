from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ActorType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Customer: "ActorType" = member("customer")
    User: "ActorType" = member("user")
    ApiKey: "ActorType" = member("api_key")
    PaddleStaff: "ActorType" = member("paddle_staff")
    Publisher: "ActorType" = member("publisher")
    System: "ActorType" = member("system")
