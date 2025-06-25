from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import (
    BillingDetails,
    CollectionMode,
    CurrencyCode,
    CustomData,
    Duration,
    ImportMeta,
    TimePeriod,
)
from paddle_billing.Notifications.Entities.Subscriptions import (
    SubscriptionDiscount,
    SubscriptionItem,
    SubscriptionScheduledChange,
    SubscriptionStatus,
)
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Subscription(SimulationEntity):
    address_id: str | Undefined = Undefined()
    billing_cycle: Duration | Undefined = Undefined()
    collection_mode: CollectionMode | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    customer_id: str | Undefined = Undefined()
    id: str | Undefined = Undefined()
    items: list[SubscriptionItem] | Undefined = Undefined()
    status: SubscriptionStatus | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    billing_details: BillingDetails | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    canceled_at: datetime | None | Undefined = Undefined()
    current_billing_period: TimePeriod | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    discount: SubscriptionDiscount | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    first_billed_at: datetime | None | Undefined = Undefined()
    next_billed_at: datetime | None | Undefined = Undefined()
    paused_at: datetime | None | Undefined = Undefined()
    scheduled_change: SubscriptionScheduledChange | None | Undefined = Undefined()
    started_at: datetime | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Subscription:
        return Subscription(
            id=data.get("id", Undefined()),
            status=SubscriptionStatus(data["status"]) if data.get("status") else Undefined(),
            customer_id=data.get("customer_id", Undefined()),
            address_id=data.get("address_id", Undefined()),
            business_id=data.get("business_id", Undefined()),
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else Undefined(),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            collection_mode=CollectionMode(data["collection_mode"]) if data.get("collection_mode") else Undefined(),
            billing_cycle=Duration.from_dict(data["billing_cycle"]) if data.get("billing_cycle") else Undefined(),
            items=(
                [SubscriptionItem.from_dict(item) for item in data["items"]]
                if isinstance(data.get("items"), list)
                else Undefined()
            ),
            billing_details=(
                BillingDetails.from_dict(data["billing_details"])
                if data.get("billing_details")
                else data.get("billing_details", Undefined())
            ),
            canceled_at=(
                datetime.fromisoformat(data["canceled_at"])
                if data.get("canceled_at")
                else data.get("canceled_at", Undefined())
            ),
            custom_data=(
                CustomData(data["custom_data"])
                if isinstance(data.get("custom_data"), dict)
                else data.get("custom_data", Undefined())
            ),
            discount=(
                SubscriptionDiscount.from_dict(data["discount"])
                if data.get("discount")
                else data.get("discount", Undefined())
            ),
            first_billed_at=(
                datetime.fromisoformat(data["first_billed_at"])
                if data.get("first_billed_at")
                else data.get("first_billed_at", Undefined())
            ),
            import_meta=(
                ImportMeta.from_dict(data["import_meta"])
                if isinstance(data.get("import_meta"), dict)
                else data.get("import_meta", Undefined())
            ),
            next_billed_at=(
                datetime.fromisoformat(data["next_billed_at"])
                if data.get("next_billed_at")
                else data.get("next_billed_at", Undefined())
            ),
            paused_at=(
                datetime.fromisoformat(data["paused_at"])
                if data.get("paused_at")
                else data.get("paused_at", Undefined())
            ),
            started_at=(
                datetime.fromisoformat(data["started_at"])
                if data.get("started_at")
                else data.get("started_at", Undefined())
            ),
            current_billing_period=(
                (
                    TimePeriod.from_dict(data["current_billing_period"])
                    if data.get("current_billing_period")
                    else data.get("current_billing_period", Undefined())
                )
            ),
            scheduled_change=(
                SubscriptionScheduledChange.from_dict(data["scheduled_change"])
                if data.get("scheduled_change")
                else data.get("scheduled_change", Undefined())
            ),
        )
