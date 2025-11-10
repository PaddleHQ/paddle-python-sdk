from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportFilterName(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Action: "ReportFilterName" = "action"
    CollectionMode: "ReportFilterName" = "collection_mode"
    CurrencyCode: "ReportFilterName" = "currency_code"
    Origin: "ReportFilterName" = "origin"
    PriceStatus: "ReportFilterName" = "price_status"
    PriceType: "ReportFilterName" = "price_type"
    PriceUpdatedAt: "ReportFilterName" = "price_updated_at"
    ProductStatus: "ReportFilterName" = "product_status"
    ProductType: "ReportFilterName" = "product_type"
    ProductUpdatedAt: "ReportFilterName" = "product_updated_at"
    RemittanceReference: "ReportFilterName" = "remittance_reference"
    Status: "ReportFilterName" = "status"
    TransactionUpdatedAt: "ReportFilterName" = "transaction_updated_at"
    Type: "ReportFilterName" = "type"
    UpdatedAt: "ReportFilterName" = "updated_at"
