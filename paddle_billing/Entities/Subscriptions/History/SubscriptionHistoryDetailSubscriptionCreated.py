from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Address import Address
from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Customer import Customer

from paddle_billing.Entities.Shared import (
    BillingDetails,
    CollectionMode,
    CurrencyCode,
    CustomData,
    Duration,
    TimePeriod,
)

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDetailItem import SubscriptionHistoryDetailItem
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDiscount import SubscriptionHistoryDiscount
from paddle_billing.Entities.Subscriptions.SubscriptionStatus import SubscriptionStatus


@dataclass
class SubscriptionHistoryDetailSubscriptionCreated:
    action: SubscriptionHistoryAction
    status: SubscriptionStatus | None
    collection_mode: CollectionMode | None
    billing_details: BillingDetails | None
    customer: Customer | None
    address: Address | None
    business: Business | None
    currency_code: CurrencyCode | None
    current_billing_period: TimePeriod | None
    billing_cycle: Duration | None
    items: list[SubscriptionHistoryDetailItem] | None
    custom_data: CustomData | None
    discount: SubscriptionHistoryDiscount | None
    has_payment_method: bool | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCreated:
        return SubscriptionHistoryDetailSubscriptionCreated(
            action=SubscriptionHistoryAction(data["action"]),
            status=SubscriptionStatus(data["status"]) if data.get("status") else None,
            collection_mode=CollectionMode(data["collection_mode"]) if data.get("collection_mode") else None,
            billing_details=(
                BillingDetails.from_dict(data["billing_details"]) if data.get("billing_details") else None
            ),
            customer=Customer.from_dict(data["customer"]) if data.get("customer") else None,
            address=Address.from_dict(data["address"]) if data.get("address") else None,
            business=Business.from_dict(data["business"]) if data.get("business") else None,
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else None,
            current_billing_period=(
                TimePeriod.from_dict(data["current_billing_period"]) if data.get("current_billing_period") else None
            ),
            billing_cycle=Duration.from_dict(data["billing_cycle"]) if data.get("billing_cycle") else None,
            items=(
                [SubscriptionHistoryDetailItem.from_dict(item) for item in data["items"]] if data.get("items") else None
            ),
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
            discount=SubscriptionHistoryDiscount.from_dict(data["discount"]) if data.get("discount") else None,
            has_payment_method=data.get("has_payment_method"),
        )
