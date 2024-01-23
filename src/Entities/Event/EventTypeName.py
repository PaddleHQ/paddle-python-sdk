from enum import StrEnum


class EventTypeName(StrEnum):
    AddressCreated           = 'address.created'
    AddressUpdated           = 'address.updated'
    AdjustmentCreated        = 'adjustment.created'
    AdjustmentUpdated        = 'adjustment.updated'
    BusinessCreated          = 'business.created'
    BusinessUpdated          = 'business.updated'
    CustomerCreated          = 'customer.created'
    CustomerUpdated          = 'customer.updated'
    DiscountCreated          = 'discount.created'
    DiscountImported         = 'discount.imported'
    DiscountUpdated          = 'discount.updated'
    InvoiceCanceled          = 'invoice.canceled'
    InvoiceCreated           = 'invoice.created'
    InvoiceIssued            = 'invoice.issued'
    InvoiceOverdue           = 'invoice.overdue'
    InvoicePaid              = 'invoice.paid'
    InvoiceScheduled         = 'invoice.scheduled'
    PayoutCreated            = 'payout.created'
    PayoutPaid               = 'payout.paid'
    PriceCreated             = 'price.created'
    PriceUpdated             = 'price.updated'
    PriceImported            = 'price.imported'
    ProductCreated           = 'product.created'
    ProductUpdated           = 'product.updated'
    ProductImported          = 'product.imported'
    SubscriptionActivated    = 'subscription.activated'
    SubscriptionCanceled     = 'subscription.canceled'
    SubscriptionCreated      = 'subscription.created'
    SubscriptionImported     = 'subscription.imported'
    SubscriptionPastDue      = 'subscription.past_due'
    SubscriptionPaused       = 'subscription.paused'
    SubscriptionResumed      = 'subscription.resumed'
    SubscriptionTrialing     = 'subscription.trialing'
    SubscriptionUpdated      = 'subscription.updated'
    TransactionBilled        = 'transaction.billed'
    TransactionCanceled      = 'transaction.canceled'
    TransactionCompleted     = 'transaction.completed'
    TransactionCreated       = 'transaction.created'
    TransactionPaid          = 'transaction.paid'
    TransactionPastDue       = 'transaction.past_due'
    TransactionPaymentFailed = 'transaction.payment_failed'
    TransactionReady         = 'transaction.ready'
    TransactionUpdated       = 'transaction.updated'
    ReportCreated            = 'report.created'
    ReportUpdated            = 'report.updated'
