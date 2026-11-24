from __future__ import annotations
from typing import Any, Union, cast

from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity as UndefinedEntity

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionActivated import (
    SubscriptionHistoryDetailSubscriptionActivated as SubscriptionHistoryDetailSubscriptionActivated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionAddressUpdated import (
    SubscriptionHistoryDetailSubscriptionAddressUpdated as SubscriptionHistoryDetailSubscriptionAddressUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingCycleUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingCycleUpdated as SubscriptionHistoryDetailSubscriptionBillingCycleUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingDateUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingDateUpdated as SubscriptionHistoryDetailSubscriptionBillingDateUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated import (
    SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated as SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessAdded import (
    SubscriptionHistoryDetailSubscriptionBusinessAdded as SubscriptionHistoryDetailSubscriptionBusinessAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessRemoved import (
    SubscriptionHistoryDetailSubscriptionBusinessRemoved as SubscriptionHistoryDetailSubscriptionBusinessRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionBusinessUpdated import (
    SubscriptionHistoryDetailSubscriptionBusinessUpdated as SubscriptionHistoryDetailSubscriptionBusinessUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCanceled import (
    SubscriptionHistoryDetailSubscriptionCanceled as SubscriptionHistoryDetailSubscriptionCanceled,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCollectionModeUpdated import (
    SubscriptionHistoryDetailSubscriptionCollectionModeUpdated as SubscriptionHistoryDetailSubscriptionCollectionModeUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionConsentRequirementGranted import (  # noqa: E501
    SubscriptionHistoryDetailSubscriptionConsentRequirementGranted as SubscriptionHistoryDetailSubscriptionConsentRequirementGranted,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCreated import (
    SubscriptionHistoryDetailSubscriptionCreated as SubscriptionHistoryDetailSubscriptionCreated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCurrencyUpdated import (
    SubscriptionHistoryDetailSubscriptionCurrencyUpdated as SubscriptionHistoryDetailSubscriptionCurrencyUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCustomDataUpdated import (
    SubscriptionHistoryDetailSubscriptionCustomDataUpdated as SubscriptionHistoryDetailSubscriptionCustomDataUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionCustomerUpdated import (
    SubscriptionHistoryDetailSubscriptionCustomerUpdated as SubscriptionHistoryDetailSubscriptionCustomerUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountAdded import (
    SubscriptionHistoryDetailSubscriptionDiscountAdded as SubscriptionHistoryDetailSubscriptionDiscountAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountExpired import (
    SubscriptionHistoryDetailSubscriptionDiscountExpired as SubscriptionHistoryDetailSubscriptionDiscountExpired,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionDiscountRemoved import (
    SubscriptionHistoryDetailSubscriptionDiscountRemoved as SubscriptionHistoryDetailSubscriptionDiscountRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemAdded import (
    SubscriptionHistoryDetailSubscriptionItemAdded as SubscriptionHistoryDetailSubscriptionItemAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemQuantityUpdated import (
    SubscriptionHistoryDetailSubscriptionItemQuantityUpdated as SubscriptionHistoryDetailSubscriptionItemQuantityUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionItemRemoved import (
    SubscriptionHistoryDetailSubscriptionItemRemoved as SubscriptionHistoryDetailSubscriptionItemRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionOneOffChargeApplied import (
    SubscriptionHistoryDetailSubscriptionOneOffChargeApplied as SubscriptionHistoryDetailSubscriptionOneOffChargeApplied,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPastDue import (
    SubscriptionHistoryDetailSubscriptionPastDue as SubscriptionHistoryDetailSubscriptionPastDue,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaused import (
    SubscriptionHistoryDetailSubscriptionPaused as SubscriptionHistoryDetailSubscriptionPaused,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentAttempted import (
    SubscriptionHistoryDetailSubscriptionPaymentAttempted as SubscriptionHistoryDetailSubscriptionPaymentAttempted,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodAdded import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodAdded as SubscriptionHistoryDetailSubscriptionPaymentMethodAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved as SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated import (
    SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated as SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionRenewed import (
    SubscriptionHistoryDetailSubscriptionRenewed as SubscriptionHistoryDetailSubscriptionRenewed,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionResumed import (
    SubscriptionHistoryDetailSubscriptionResumed as SubscriptionHistoryDetailSubscriptionResumed,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeAdded import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeAdded as SubscriptionHistoryDetailSubscriptionScheduledChangeAdded,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved as SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved,
)
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated import (
    SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated as SubscriptionHistoryDetailSubscriptionScheduledChangeUpdated,
)

_KnownSubscriptionHistoryDetail = Union[
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
]

SubscriptionHistoryDetailUnion = Union[_KnownSubscriptionHistoryDetail, UndefinedEntity]


class SubscriptionHistoryDetail:
    """
    Dispatches a subscription history `detail` payload to the dataclass matching its `action`.

    Unrecognised actions (for example, added by the API after this SDK version was released)
    hydrate as an `UndefinedEntity` wrapping the raw dictionary.
    """

    _CLASSES: dict[str, type[_KnownSubscriptionHistoryDetail]] = {
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
        detail_class = SubscriptionHistoryDetail._CLASSES.get(cast(str, data.get("action")))

        if detail_class is None:
            return UndefinedEntity(data)

        return detail_class.from_dict(data)
