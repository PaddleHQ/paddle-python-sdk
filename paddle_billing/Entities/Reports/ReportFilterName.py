from enum import StrEnum


class ReportFilterName(StrEnum):
    CollectionMode = 'collection_mode'
    CurrencyCode   = 'currency_code'
    Origin         = 'origin'
    Status         = 'status'
    UpdatedAt      = 'updated_at'
