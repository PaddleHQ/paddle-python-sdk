from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Address import Address

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionAddressUpdated:
    action: SubscriptionHistoryAction
    address: Address

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionAddressUpdated:
        return SubscriptionHistoryDetailSubscriptionAddressUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            address=Address.from_dict(data["address"]),
        )
