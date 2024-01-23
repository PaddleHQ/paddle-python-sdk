from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional


@dataclass
class SubscriptionManagementUrls:
    updatePaymentMethod: Optional[str]
    cancel:              str


    @staticmethod
    def from_dict(data: dict) -> SubscriptionManagementUrls:
        return SubscriptionManagementUrls(
            updatePaymentMethod = data.get('update_payment_method'),
            cancel              = data['cancel'],
        )
