# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/NotificationSettings/NotificationSettingsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import NotificationSettingCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return NotificationSettingCollection.from_list(
                parser.get_list(),
                self.client._make_paginator(parser.get_pagination(), NotificationSettingCollection),
            )
        return await self.client._get("/notification-settings", operation.get_parameters(), parse)

    async def get(self, notification_setting_id: str) -> NotificationSetting:
        def parse(response):
            self.response = response
            return NotificationSetting.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/notification-settings/{notification_setting_id}", None, parse)

    async def create(self, operation: CreateNotificationSetting) -> NotificationSetting:
        def parse(response):
            self.response = response
            return NotificationSetting.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/notification-settings", operation, parse)

    async def update(self, notification_setting_id: str, operation: UpdateNotificationSetting) -> NotificationSetting:
        def parse(response):
            self.response = response
            return NotificationSetting.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/notification-settings/{notification_setting_id}", operation, parse)

    async def delete(self, notification_setting_id: str) -> None:
        self.client._delete(f"/notification-settings/{notification_setting_id}")

        return None
