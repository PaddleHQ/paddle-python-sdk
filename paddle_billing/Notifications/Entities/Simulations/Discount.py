from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Discount import DiscountMode
from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Discounts import DiscountStatus, DiscountType
from paddle_billing.Notifications.Entities.Shared import CurrencyCode, CustomData, ImportMeta
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Discount(SimulationEntity):
    amount: str | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    description: str | Undefined = Undefined()
    enabled_for_checkout: bool | Undefined = Undefined()
    id: str | Undefined = Undefined()
    recur: bool | Undefined = Undefined()
    status: DiscountStatus | Undefined = Undefined()
    type: DiscountType | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    code: str | None | Undefined = Undefined()
    currency_code: CurrencyCode | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    expires_at: datetime | None | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()
    maximum_recurring_intervals: int | None | Undefined = Undefined()
    restrict_to: list[Any] | None | Undefined = Undefined()
    usage_limit: int | None | Undefined = Undefined()
    mode: DiscountMode | None | Undefined = Undefined()
    discount_group_id: str | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Discount:
        return Discount(
            amount=data.get("amount", Undefined()),
            code=data.get("code", Undefined()),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            description=data.get("description", Undefined()),
            enabled_for_checkout=data.get("enabled_for_checkout", Undefined()),
            id=data.get("id", Undefined()),
            maximum_recurring_intervals=data.get("maximum_recurring_intervals", Undefined()),
            usage_limit=data.get("usage_limit", Undefined()),
            recur=data.get("recur", Undefined()),
            restrict_to=data.get("restrict_to", Undefined()),
            status=DiscountStatus(data["status"]) if data.get("status") else Undefined(),
            type=DiscountType(data["type"]) if data.get("type") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            currency_code=(
                CurrencyCode(data["currency_code"])
                if data.get("currency_code")
                else data.get("currency_code", Undefined())
            ),
            custom_data=(
                CustomData(data["custom_data"])
                if isinstance(data.get("custom_data"), dict)
                else data.get("custom_data", Undefined())
            ),
            expires_at=(
                datetime.fromisoformat(data["expires_at"])
                if data.get("expires_at")
                else data.get("expires_at", Undefined())
            ),
            import_meta=(
                ImportMeta.from_dict(data["import_meta"])
                if isinstance(data.get("import_meta"), dict)
                else data.get("import_meta", Undefined())
            ),
            mode=DiscountMode(data["mode"]) if data.get("mode") else Undefined(),
            discount_group_id=data.get("discount_group_id", Undefined()),
        )
