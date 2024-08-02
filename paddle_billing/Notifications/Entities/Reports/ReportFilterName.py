from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportFilterName(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Action           = 'action'
    CollectionMode   = 'collection_mode'
    CurrencyCode     = 'currency_code'
    Origin           = 'origin'
    PriceStatus      = 'price_status'
    PriceType        = 'price_type'
    PriceUpdatedAt   = 'price_updated_at'
    ProductStatus    = 'product_status'
    ProductType      = 'product_type'
    ProductUpdatedAt = 'product_updated_at'
    Status           = 'status'
    Type             = 'type'
    UpdatedAt        = 'updated_at'
