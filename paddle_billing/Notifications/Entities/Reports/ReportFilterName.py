from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ReportFilterName(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Action: "ReportFilterName" = member("action")
    BalanceMovementDate: "ReportFilterName" = member("balance_movement_date")
    BalanceMovementType: "ReportFilterName" = member("balance_movement_type")
    CheckoutCreatedAt: "ReportFilterName" = member("checkout_created_at")
    CollectionMode: "ReportFilterName" = member("collection_mode")
    CurrencyCode: "ReportFilterName" = member("currency_code")
    CustomerCountryCode: "ReportFilterName" = member("customer_country_code")
    Origin: "ReportFilterName" = member("origin")
    PriceStatus: "ReportFilterName" = member("price_status")
    PriceType: "ReportFilterName" = member("price_type")
    PriceUpdatedAt: "ReportFilterName" = member("price_updated_at")
    ProductStatus: "ReportFilterName" = member("product_status")
    ProductType: "ReportFilterName" = member("product_type")
    ProductUpdatedAt: "ReportFilterName" = member("product_updated_at")
    RemittanceReference: "ReportFilterName" = member("remittance_reference")
    Status: "ReportFilterName" = member("status")
    SubscriptionCreatedAt: "ReportFilterName" = member("subscription_created_at")
    SubscriptionScheduledChangeAction: "ReportFilterName" = member("subscription_scheduled_change_action")
    SubscriptionStatus: "ReportFilterName" = member("subscription_status")
    TransactionUpdatedAt: "ReportFilterName" = member("transaction_updated_at")
    Type: "ReportFilterName" = member("type")
    UpdatedAt: "ReportFilterName" = member("updated_at")
