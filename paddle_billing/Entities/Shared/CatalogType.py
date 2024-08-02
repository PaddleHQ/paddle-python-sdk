from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CatalogType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard = 'standard'
    Custom   = 'custom'
