from __future__ import annotations
from typing import Any, Union

from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionActivated import (
    SubscriptionHistoryDetailSubscriptionActivated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionAddressUpdated import (
    SubscriptionHistoryDetailSubscriptionAddressUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingCycleUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingCycleUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingDateUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingDateUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessAdded import (
    SubscriptionHistoryDetailSubscriptionBusinessAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessRemoved import (
    SubscriptionHistoryDetailSubscriptionBusinessRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessUpdated import (
    SubscriptionHistoryDetailSubscriptionBusinessUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCanceled import (
    SubscriptionHistoryDetailSubscriptionCanceled,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCollectionModeUpdated import (
    SubscriptionHistoryDetailSubscriptionCollectionModeUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionConsentRequirementGranted import (  # noqa: E501
    SubscriptionHistoryDetailSubscriptionConsentRequirementGranted,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCreated import (
    SubscriptionHistoryDetailSubscriptionCreated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCurrencyUpdated import (
    SubscriptionHistoryDetailSubscriptionCurrencyUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCustomDataUpdated import (
    SubscriptionHistoryDetailSubscriptionCustomDataUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCustomerUpdated import (
    SubscriptionHistoryDetailSubscriptionCustomerUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountAdded import (
    SubscriptionHistoryDetailSubscriptionDiscountAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountExpired import (
    SubscriptionHistoryDetailSubscriptionDiscountExpired,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountRemoved import (
    SubscriptionHistoryDetailSubscriptionDiscountRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemAdded import (
    SubscriptionHistoryDetailSubscriptionItemAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemQuantityUpdated import (
    SubscriptionHistoryDetailSubscriptionItemQuantityUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemRemoved import (
    SubscriptionHistoryDetailSubscriptionItemRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionOneOffChargeApplied import (
    SubscriptionHistoryDetailSubscriptionOneOffChargeApplied,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPastDue import (
    SubscriptionHistoryDetailSubscriptionPastDue,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaused import (
    SubscriptionHistoryDetailSubscriptionPaused,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentAttempted import (
    SubscriptionHistoryDetailSubscriptionPaymentAttempted,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodAdded import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionRenewed import (
    SubscriptionHistoryDetailSubscriptionRenewed,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionResumed import (
    SubscriptionHistoryDetailSubscriptionResumed,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeAdded import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated,
)

SubscriptionHistoryDetailUnion = Union[
    SubscriptionHistoryDetailSubscriptionActivated,
    SubscriptionHistoryDetailSubscriptionAddressUpdated,
    SubscriptionHistoryDetailSubscriptionBillingCycleUpdated,
    SubscriptionHistoryDetailSubscriptionBillingDateUpdated,
    SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated,
    SubscriptionHistoryDetailSubscriptionBusinessAdded,
    SubscriptionHistoryDetailSubscriptionBusinessRemoved,
    SubscriptionHistoryDetailSubscriptionBusinessUpdated,
    SubscriptionHistoryDetailSubscriptionCanceled,
    SubscriptionHistoryDetailSubscriptionCollectionModeUpdated,
    SubscriptionHistoryDetailSubscriptionConsentRequirementGranted,
    SubscriptionHistoryDetailSubscriptionCreated,
    SubscriptionHistoryDetailSubscriptionCurrencyUpdated,
    SubscriptionHistoryDetailSubscriptionCustomDataUpdated,
    SubscriptionHistoryDetailSubscriptionCustomerUpdated,
    SubscriptionHistoryDetailSubscriptionDiscountAdded,
    SubscriptionHistoryDetailSubscriptionDiscountExpired,
    SubscriptionHistoryDetailSubscriptionDiscountRemoved,
    SubscriptionHistoryDetailSubscriptionItemAdded,
    SubscriptionHistoryDetailSubscriptionItemQuantityUpdated,
    SubscriptionHistoryDetailSubscriptionItemRemoved,
    SubscriptionHistoryDetailSubscriptionOneOffChargeApplied,
    SubscriptionHistoryDetailSubscriptionPastDue,
    SubscriptionHistoryDetailSubscriptionPaused,
    SubscriptionHistoryDetailSubscriptionPaymentAttempted,
    SubscriptionHistoryDetailSubscriptionPaymentMethodAdded,
    SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved,
    SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated,
    SubscriptionHistoryDetailSubscriptionRenewed,
    SubscriptionHistoryDetailSubscriptionResumed,
    SubscriptionHistoryDetailSubscriptionScheduledChangeAdded,
    SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved,
    SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated,
    UndefinedEntity,
]


class SubscriptionHistoryDetail:
    """
    Dispatches a subscription history `detail` payload to the dataclass matching its `action`.

    Unrecognised actions (for example, added by the API after this SDK version was released)
    hydrate as an `UndefinedEntity` wrapping the raw dictionary.
    """

    _CLASSES: dict[str, type] = {
        "subscription_activated": SubscriptionHistoryDetailSubscriptionActivated,
        "subscription_address_updated": SubscriptionHistoryDetailSubscriptionAddressUpdated,
        "subscription_billing_cycle_updated": SubscriptionHistoryDetailSubscriptionBillingCycleUpdated,
        "subscription_billing_date_updated": SubscriptionHistoryDetailSubscriptionBillingDateUpdated,
        "subscription_billing_details_updated": SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated,
        "subscription_business_added": SubscriptionHistoryDetailSubscriptionBusinessAdded,
        "subscription_business_removed": SubscriptionHistoryDetailSubscriptionBusinessRemoved,
        "subscription_business_updated": SubscriptionHistoryDetailSubscriptionBusinessUpdated,
        "subscription_canceled": SubscriptionHistoryDetailSubscriptionCanceled,
        "subscription_collection_mode_updated": SubscriptionHistoryDetailSubscriptionCollectionModeUpdated,
        "subscription_consent_requirement_granted": SubscriptionHistoryDetailSubscriptionConsentRequirementGranted,
        "subscription_created": SubscriptionHistoryDetailSubscriptionCreated,
        "subscription_currency_updated": SubscriptionHistoryDetailSubscriptionCurrencyUpdated,
        "subscription_custom_data_updated": SubscriptionHistoryDetailSubscriptionCustomDataUpdated,
        "subscription_customer_updated": SubscriptionHistoryDetailSubscriptionCustomerUpdated,
        "subscription_discount_added": SubscriptionHistoryDetailSubscriptionDiscountAdded,
        "subscription_discount_expired": SubscriptionHistoryDetailSubscriptionDiscountExpired,
        "subscription_discount_removed": SubscriptionHistoryDetailSubscriptionDiscountRemoved,
        "subscription_item_added": SubscriptionHistoryDetailSubscriptionItemAdded,
        "subscription_item_quantity_updated": SubscriptionHistoryDetailSubscriptionItemQuantityUpdated,
        "subscription_item_removed": SubscriptionHistoryDetailSubscriptionItemRemoved,
        "subscription_one_off_charge_applied": SubscriptionHistoryDetailSubscriptionOneOffChargeApplied,
        "subscription_past_due": SubscriptionHistoryDetailSubscriptionPastDue,
        "subscription_paused": SubscriptionHistoryDetailSubscriptionPaused,
        "subscription_payment_attempted": SubscriptionHistoryDetailSubscriptionPaymentAttempted,
        "subscription_payment_method_added": SubscriptionHistoryDetailSubscriptionPaymentMethodAdded,
        "subscription_payment_method_removed": SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved,
        "subscription_payment_method_updated": SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated,
        "subscription_renewed": SubscriptionHistoryDetailSubscriptionRenewed,
        "subscription_resumed": SubscriptionHistoryDetailSubscriptionResumed,
        "subscription_scheduled_change_added": SubscriptionHistoryDetailSubscriptionScheduledChangeAdded,
        "subscription_scheduled_change_removed": SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved,
        "subscription_scheduled_change_updated": SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated,
    }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailUnion:
        detail_class = SubscriptionHistoryDetail._CLASSES.get(data.get("action"))

        if detail_class is None:
            return UndefinedEntity(data)

        return detail_class.from_dict(data)
