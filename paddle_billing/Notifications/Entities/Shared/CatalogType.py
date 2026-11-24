from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CatalogType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "CatalogType" = member("standard")
    Custom: "CatalogType" = member("custom")
