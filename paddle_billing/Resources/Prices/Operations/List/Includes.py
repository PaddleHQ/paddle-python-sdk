from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Product: "Includes" = member("product")
