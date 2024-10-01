from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CatalogType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "CatalogType" = "standard"
    Custom: "CatalogType" = "custom"
