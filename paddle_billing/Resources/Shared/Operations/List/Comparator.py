from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Comparator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    LT: "Comparator" = "LT"
    LTE: "Comparator" = "LTE"
    GT: "Comparator" = "GT"
    GTE: "Comparator" = "GTE"
