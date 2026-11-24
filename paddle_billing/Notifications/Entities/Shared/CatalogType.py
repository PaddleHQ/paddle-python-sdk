from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CatalogType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "CatalogType" = member("standard")
    Custom: "CatalogType" = member("custom")
