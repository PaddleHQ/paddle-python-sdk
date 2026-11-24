from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionHistoryAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionActivated: "SubscriptionHistoryAction" = member("subscription_activated")
    SubscriptionAddressUpdated: "SubscriptionHistoryAction" = member("subscription_address_updated")
    SubscriptionBillingCycleUpdated: "SubscriptionHistoryAction" = member("subscription_billing_cycle_updated")
    SubscriptionBillingDateUpdated: "SubscriptionHistoryAction" = member("subscription_billing_date_updated")
    SubscriptionBillingDetailsUpdated: "SubscriptionHistoryAction" = member("subscription_billing_details_updated")
    SubscriptionBusinessAdded: "SubscriptionHistoryAction" = member("subscription_business_added")
    SubscriptionBusinessRemoved: "SubscriptionHistoryAction" = member("subscription_business_removed")
    SubscriptionBusinessUpdated: "SubscriptionHistoryAction" = member("subscription_business_updated")
    SubscriptionCanceled: "SubscriptionHistoryAction" = member("subscription_canceled")
    SubscriptionCollectionModeUpdated: "SubscriptionHistoryAction" = member("subscription_collection_mode_updated")
    SubscriptionConsentRequirementGranted: "SubscriptionHistoryAction" = member(
        "subscription_consent_requirement_granted"
    )
    SubscriptionCreated: "SubscriptionHistoryAction" = member("subscription_created")
    SubscriptionCurrencyUpdated: "SubscriptionHistoryAction" = member("subscription_currency_updated")
    SubscriptionCustomDataUpdated: "SubscriptionHistoryAction" = member("subscription_custom_data_updated")
    SubscriptionCustomerUpdated: "SubscriptionHistoryAction" = member("subscription_customer_updated")
    SubscriptionDiscountAdded: "SubscriptionHistoryAction" = member("subscription_discount_added")
    SubscriptionDiscountExpired: "SubscriptionHistoryAction" = member("subscription_discount_expired")
    SubscriptionDiscountRemoved: "SubscriptionHistoryAction" = member("subscription_discount_removed")
    SubscriptionItemAdded: "SubscriptionHistoryAction" = member("subscription_item_added")
    SubscriptionItemQuantityUpdated: "SubscriptionHistoryAction" = member("subscription_item_quantity_updated")
    SubscriptionItemRemoved: "SubscriptionHistoryAction" = member("subscription_item_removed")
    SubscriptionOneOffChargeApplied: "SubscriptionHistoryAction" = member("subscription_one_off_charge_applied")
    SubscriptionPastDue: "SubscriptionHistoryAction" = member("subscription_past_due")
    SubscriptionPaused: "SubscriptionHistoryAction" = member("subscription_paused")
    SubscriptionPaymentAttempted: "SubscriptionHistoryAction" = member("subscription_payment_attempted")
    SubscriptionPaymentMethodAdded: "SubscriptionHistoryAction" = member("subscription_payment_method_added")
    SubscriptionPaymentMethodRemoved: "SubscriptionHistoryAction" = member("subscription_payment_method_removed")
    SubscriptionPaymentMethodUpdated: "SubscriptionHistoryAction" = member("subscription_payment_method_updated")
    SubscriptionRenewed: "SubscriptionHistoryAction" = member("subscription_renewed")
    SubscriptionResumed: "SubscriptionHistoryAction" = member("subscription_resumed")
    SubscriptionScheduledChangeAdded: "SubscriptionHistoryAction" = member("subscription_scheduled_change_added")
    SubscriptionScheduledChangeRemoved: "SubscriptionHistoryAction" = member("subscription_scheduled_change_removed")
    SubscriptionScheduledChangeUpdated: "SubscriptionHistoryAction" = member("subscription_scheduled_change_updated")
