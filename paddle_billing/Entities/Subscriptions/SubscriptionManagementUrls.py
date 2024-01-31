from __future__  import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionManagementUrls:
    update_payment_method: str | None
    cancel:                str


    @staticmethod
    def from_dict(data: dict) -> SubscriptionManagementUrls:
        return SubscriptionManagementUrls(
            update_payment_method = data.get('update_payment_method'),
            cancel                = data['cancel'],
        )
