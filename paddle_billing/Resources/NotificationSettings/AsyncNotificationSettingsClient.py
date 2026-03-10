from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, NotificationSettingCollection
from paddle_billing.Entities.NotificationSetting import NotificationSetting

from paddle_billing.Resources.NotificationSettings.Operations import (
    CreateNotificationSetting,
    UpdateNotificationSetting,
    ListNotificationSettings,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncNotificationSettingsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListNotificationSettings | None = None) -> NotificationSettingCollection:
        if operation is None:
            operation = ListNotificationSettings()

        self.response = await self.client.get_raw("/notification-settings", operation.get_parameters())
        parser = ResponseParser(self.response)

        return NotificationSettingCollection.from_list(
            parser.get_list(),
            AsyncPaginator(self.client, parser.get_pagination(), NotificationSettingCollection),
        )

    async def get(self, notification_setting_id: str) -> NotificationSetting:
        self.response = await self.client.get_raw(f"/notification-settings/{notification_setting_id}")
        parser = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_dict())

    async def create(self, operation: CreateNotificationSetting) -> NotificationSetting:
        self.response = await self.client.post_raw("/notification-settings", operation)
        parser = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_dict())

    async def update(self, notification_setting_id: str, operation: UpdateNotificationSetting) -> NotificationSetting:
        self.response = await self.client.patch_raw(f"/notification-settings/{notification_setting_id}", operation)
        parser = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_dict())

    async def delete(self, notification_setting_id: str) -> None:
        self.response = await self.client.delete_raw(f"/notification-settings/{notification_setting_id}")

        return None
