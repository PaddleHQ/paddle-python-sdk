from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CollectionMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Automatic = 'automatic'
    Manual    = 'manual'
