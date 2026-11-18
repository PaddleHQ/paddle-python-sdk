from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CollectionMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Automatic: "CollectionMode" = member("automatic")
    Manual: "CollectionMode" = member("manual")
