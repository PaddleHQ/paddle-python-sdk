from paddle_billing.PaddleStrEnum import PaddleStrEnum


class ReportFilterName(PaddleStrEnum):
    Action         = 'action'
    CollectionMode = 'collection_mode'
    CurrencyCode   = 'currency_code'
    Origin         = 'origin'
    Status         = 'status'
    UpdatedAt      = 'updated_at'
