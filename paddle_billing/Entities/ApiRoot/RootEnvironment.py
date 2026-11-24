from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class RootEnvironment(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Production: "RootEnvironment" = member("production")
    Sandbox: "RootEnvironment" = member("sandbox")
