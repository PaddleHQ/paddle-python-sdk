from __future__  import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionManagementUrls:
    updatePaymentMethod: str | None
    cancel:              str


    @staticmethod
    def from_dict(data: dict) -> SubscriptionManagementUrls:
        return SubscriptionManagementUrls(
            updatePaymentMethod = data.get('update_payment_method'),
            cancel              = data['cancel'],
        )
