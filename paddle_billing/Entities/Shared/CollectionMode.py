from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CollectionMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Automatic: "CollectionMode" = "automatic"
    Manual: "CollectionMode" = "manual"
