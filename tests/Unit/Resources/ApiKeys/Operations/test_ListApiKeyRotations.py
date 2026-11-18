from paddle_billing.Resources.ApiKeys.Operations import ListApiKeyRotations
from paddle_billing.Resources.Shared.Operations import OrderBy, Pager


class TestListApiKeyRotations:
    def test_does_not_send_order_by(self):
        operation = ListApiKeyRotations(
            Pager(after="apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7", order_by=OrderBy.id_descending())
        )

        assert operation.get_parameters() == {"after": "apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7", "per_page": 50}
