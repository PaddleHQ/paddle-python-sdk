from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, NotificationCollection
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

        self.response = await self.client.get_raw("/notifications", operation.get_parameters())
        parser = ResponseParser(self.response)

        return NotificationCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), NotificationCollection)
        )

    async def get(self, notification_id: str) -> Notification:
        self.response = await self.client.get_raw(f"/notifications/{notification_id}")
        parser = ResponseParser(self.response)

        return Notification.from_dict(parser.get_dict())

    async def replay(self, notification_id: str) -> str:
        self.response = await self.client.post_raw(f"/notifications/{notification_id}/replay")
        parser = ResponseParser(self.response)
        data = parser.get_data()

        return data.get("notification_id", "")
