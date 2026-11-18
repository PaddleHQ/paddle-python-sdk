from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Prices: "Includes" = member("prices")
