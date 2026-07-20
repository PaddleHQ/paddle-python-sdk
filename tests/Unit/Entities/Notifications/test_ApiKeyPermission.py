from json import loads

from paddle_billing.Notifications.Entities.ApiKey import ApiKey
from paddle_billing.Notifications.Entities.ApiKeys import ApiKeyPermission

from tests.Utils.ReadsFixture import ReadsFixtures


class TestApiKeyPermission:
    def test_subscription_history_read_is_a_known_permission(self):
        permission = ApiKeyPermission("subscription_history.read")

        assert permission.is_known()
        assert permission == ApiKeyPermission.SubscriptionHistoryRead
        assert permission.name == "SubscriptionHistoryRead"

    def test_api_key_entity_hydrates_subscription_history_read_permission(self):
        entity = ApiKey.from_dict(loads(ReadsFixtures.read_raw_json_fixture("notification/entity/api_key.created")))

        assert ApiKeyPermission.SubscriptionHistoryRead in entity.permissions
