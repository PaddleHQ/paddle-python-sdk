from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Shared import (
    BillingDetails,
    Checkout,
    CollectionMode,
    CurrencyCode,
    CustomData,
    TimePeriod,
    TransactionOrigin,
    TransactionPaymentAttempt,
    TransactionStatus,
)

from paddle_billing.Notifications.Entities.Transactions.TransactionDetails import TransactionDetails
from paddle_billing.Notifications.Entities.Transactions.TransactionItem import TransactionItem
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Transaction(SimulationEntity):
    id: str | Undefined = Undefined()
    status: TransactionStatus | Undefined = Undefined()
    customer_id: str | None | Undefined = Undefined()
    address_id: str | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    origin: TransactionOrigin | Undefined = Undefined()
    subscription_id: str | None | Undefined = Undefined()
    invoice_id: str | None | Undefined = Undefined()
    invoice_number: str | None | Undefined = Undefined()
    collection_mode: CollectionMode | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    billing_details: BillingDetails | None | Undefined = Undefined()
    billing_period: TimePeriod | None | Undefined = Undefined()
    items: list[TransactionItem] | Undefined = Undefined()
    details: TransactionDetails | Undefined = Undefined()
    payments: list[TransactionPaymentAttempt] | Undefined = Undefined()
    checkout: Checkout | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    billed_at: datetime | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict) -> Transaction:
        return Transaction(
            address_id=data.get("address_id", Undefined()),
            business_id=data.get("business_id", Undefined()),
            collection_mode=CollectionMode(data["collection_mode"]) if data.get("collection_mode") else Undefined(),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else Undefined(),
            customer_id=data.get("customer_id", Undefined()),
            details=TransactionDetails.from_dict(data["details"]) if data.get("details") else Undefined(),
            discount_id=data.get("discount_id", Undefined()),
            id=data.get("id", Undefined()),
            invoice_id=data.get("invoice_id", Undefined()),
            invoice_number=data.get("invoice_number", Undefined()),
            origin=TransactionOrigin(data["origin"]) if data.get("origin") else Undefined(),
            status=TransactionStatus(data["status"]) if data.get("status") else Undefined(),
            subscription_id=data.get("subscription_id", Undefined()),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            items=(
                [TransactionItem.from_dict(item) for item in data["items"]]
                if isinstance(data.get("items"), list)
                else Undefined()
            ),
            payments=(
                [TransactionPaymentAttempt.from_dict(item) for item in data["payments"]]
                if isinstance(data.get("payments"), list)
                else Undefined()
            ),
            billed_at=(
                datetime.fromisoformat(data["billed_at"])
                if data.get("billed_at")
                else data.get("billed_at", Undefined())
            ),
            billing_details=(
                BillingDetails.from_dict(data["billing_details"])
                if data.get("billing_details")
                else data.get("billing_details", Undefined())
            ),
            billing_period=(
                TimePeriod.from_dict(data["billing_period"])
                if data.get("billing_period")
                else data.get("billing_period", Undefined())
            ),
            custom_data=(
                CustomData(data["custom_data"])
                if isinstance(data.get("custom_data"), dict)
                else data.get("custom_data", Undefined())
            ),
            checkout=(
                Checkout.from_dict(data["checkout"]) if data.get("checkout") else data.get("checkout", Undefined())
            ),
        )
