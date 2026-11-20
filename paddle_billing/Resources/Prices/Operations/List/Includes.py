from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Product: "Includes" = member("product")
