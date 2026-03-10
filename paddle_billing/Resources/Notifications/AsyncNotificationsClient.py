# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Notifications/NotificationsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import NotificationCollection
from paddle_billing.Entities.Notification import Notification

from paddle_billing.Resources.Notifications.Operations import ListNotifications

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncNotificationsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListNotifications | None = None) -> NotificationCollection:
        if operation is None:
            operation = ListNotifications()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return NotificationCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), NotificationCollection)
            )
        return await self.client._get("/notifications", operation.get_parameters(), parse)

    async def get(self, notification_id: str) -> Notification:
        def parse(response):
            self.response = response
            return Notification.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/notifications/{notification_id}", None, parse)

    async def replay(self, notification_id: str) -> str:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            data = parser.get_data()
            return data.get("notification_id", "")
        return await self.client._post(f"/notifications/{notification_id}/replay", None, parse)
