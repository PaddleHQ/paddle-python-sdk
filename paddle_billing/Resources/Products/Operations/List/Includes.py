# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Prices: "Includes" = "prices"
