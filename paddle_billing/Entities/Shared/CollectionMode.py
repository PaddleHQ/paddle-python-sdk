from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CollectionMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Automatic: "CollectionMode" = member("automatic")
    Manual: "CollectionMode" = member("manual")
