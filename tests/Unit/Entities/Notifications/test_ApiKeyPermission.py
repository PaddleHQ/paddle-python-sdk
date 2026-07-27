from json import loads

from pytest import mark

from paddle_billing.Notifications.Entities.ApiKey import ApiKey
from paddle_billing.Notifications.Entities.ApiKeys import ApiKeyPermission

from tests.Utils.ReadsFixture import ReadsFixtures


class TestApiKeyPermission:
    @mark.parametrize(
        "value, expected_name",
        [
            ("checkout_domain.read", "CheckoutDomainRead"),
            ("checkout_domain.write", "CheckoutDomainWrite"),
            ("client_token.read", "ClientTokenRead"),
            ("client_token.write", "ClientTokenWrite"),
            ("metrics.read", "MetricsRead"),
            ("subscription_history.read", "SubscriptionHistoryRead"),
        ],
    )
    def test_permission_is_known(self, value, expected_name):
        permission = ApiKeyPermission(value)

        assert permission.is_known()
        assert permission.name == expected_name
        assert permission == getattr(ApiKeyPermission, expected_name)

    def test_api_key_entity_hydrates_new_permissions(self):
        entity = ApiKey.from_dict(loads(ReadsFixtures.read_raw_json_fixture("notification/entity/api_key.created")))

        for permission in [
            ApiKeyPermission.CheckoutDomainRead,
            ApiKeyPermission.ClientTokenRead,
            ApiKeyPermission.MetricsRead,
            ApiKeyPermission.SubscriptionHistoryRead,
        ]:
            assert permission in entity.permissions
