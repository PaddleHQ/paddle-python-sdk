from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Comparator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    LT: "Comparator" = member("LT")
    LTE: "Comparator" = member("LTE")
    GT: "Comparator" = member("GT")
    GTE: "Comparator" = member("GTE")
