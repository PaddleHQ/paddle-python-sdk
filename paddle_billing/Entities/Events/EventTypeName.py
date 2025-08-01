from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class EventTypeName(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AddressCreated: "EventTypeName" = "address.created"
    AddressImported: "EventTypeName" = "address.imported"
    AddressUpdated: "EventTypeName" = "address.updated"
    AdjustmentCreated: "EventTypeName" = "adjustment.created"
    AdjustmentUpdated: "EventTypeName" = "adjustment.updated"
    ApiKeyCreated: "EventTypeName" = "api_key.created"
    ApiKeyExpired: "EventTypeName" = "api_key.expired"
    ApiKeyExpiring: "EventTypeName" = "api_key.expiring"
    ApiKeyRevoked: "EventTypeName" = "api_key.revoked"
    ApiKeyUpdated: "EventTypeName" = "api_key.updated"
    BusinessCreated: "EventTypeName" = "business.created"
    BusinessImported: "EventTypeName" = "business.imported"
    BusinessUpdated: "EventTypeName" = "business.updated"
    ClientTokenCreated: "EventTypeName" = "client_token.created"
    ClientTokenRevoked: "EventTypeName" = "client_token.revoked"
    ClientTokenUpdated: "EventTypeName" = "client_token.updated"
    CustomerCreated: "EventTypeName" = "customer.created"
    CustomerImported: "EventTypeName" = "customer.imported"
    CustomerUpdated: "EventTypeName" = "customer.updated"
    DiscountCreated: "EventTypeName" = "discount.created"
    DiscountImported: "EventTypeName" = "discount.imported"
    DiscountUpdated: "EventTypeName" = "discount.updated"
    DiscountGroupCreated: "EventTypeName" = "discount_group.created"
    DiscountGroupUpdated: "EventTypeName" = "discount_group.updated"
    InvoiceCanceled: "EventTypeName" = "invoice.canceled"
    InvoiceCreated: "EventTypeName" = "invoice.created"
    InvoiceIssued: "EventTypeName" = "invoice.issued"
    InvoiceOverdue: "EventTypeName" = "invoice.overdue"
    InvoicePaid: "EventTypeName" = "invoice.paid"
    InvoiceScheduled: "EventTypeName" = "invoice.scheduled"
    PaymentMethodDeleted: "EventTypeName" = "payment_method.deleted"
    PaymentMethodSaved: "EventTypeName" = "payment_method.saved"
    PayoutCreated: "EventTypeName" = "payout.created"
    PayoutPaid: "EventTypeName" = "payout.paid"
    PriceCreated: "EventTypeName" = "price.created"
    PriceUpdated: "EventTypeName" = "price.updated"
    PriceImported: "EventTypeName" = "price.imported"
    ProductCreated: "EventTypeName" = "product.created"
    ProductUpdated: "EventTypeName" = "product.updated"
    ProductImported: "EventTypeName" = "product.imported"
    SubscriptionActivated: "EventTypeName" = "subscription.activated"
    SubscriptionCanceled: "EventTypeName" = "subscription.canceled"
    SubscriptionCreated: "EventTypeName" = "subscription.created"
    SubscriptionImported: "EventTypeName" = "subscription.imported"
    SubscriptionPastDue: "EventTypeName" = "subscription.past_due"
    SubscriptionPaused: "EventTypeName" = "subscription.paused"
    SubscriptionResumed: "EventTypeName" = "subscription.resumed"
    SubscriptionTrialing: "EventTypeName" = "subscription.trialing"
    SubscriptionUpdated: "EventTypeName" = "subscription.updated"
    TransactionBilled: "EventTypeName" = "transaction.billed"
    TransactionCanceled: "EventTypeName" = "transaction.canceled"
    TransactionCompleted: "EventTypeName" = "transaction.completed"
    TransactionCreated: "EventTypeName" = "transaction.created"
    TransactionPaid: "EventTypeName" = "transaction.paid"
    TransactionPastDue: "EventTypeName" = "transaction.past_due"
    TransactionPaymentFailed: "EventTypeName" = "transaction.payment_failed"
    TransactionReady: "EventTypeName" = "transaction.ready"
    TransactionRevised: "EventTypeName" = "transaction.revised"
    TransactionUpdated: "EventTypeName" = "transaction.updated"
    ReportCreated: "EventTypeName" = "report.created"
    ReportUpdated: "EventTypeName" = "report.updated"
