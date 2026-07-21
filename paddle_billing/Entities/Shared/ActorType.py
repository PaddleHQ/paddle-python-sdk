from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ActorType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Customer: "ActorType" = "customer"
    User: "ActorType" = "user"
    ApiKey: "ActorType" = "api_key"
    PaddleStaff: "ActorType" = "paddle_staff"
    Publisher: "ActorType" = "publisher"
    System: "ActorType" = "system"
