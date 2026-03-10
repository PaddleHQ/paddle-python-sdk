from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, NotificationLogCollection
from paddle_billing.Resources.NotificationLogs.Operations import ListNotificationLogs

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncNotificationLogsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(
        self, notification_id: str, operation: ListNotificationLogs | None = None
    ) -> NotificationLogCollection:
        if operation is None:
            operation = ListNotificationLogs()

        self.response = await self.client.get_raw(
            f"/notifications/{notification_id}/logs", operation.get_parameters()
        )
        parser = ResponseParser(self.response)

        return NotificationLogCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), NotificationLogCollection)
        )
