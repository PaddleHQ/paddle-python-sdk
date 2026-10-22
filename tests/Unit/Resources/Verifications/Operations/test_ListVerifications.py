from pytest import raises

from paddle_billing.Entities.Verifications import VerificationType

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager
from paddle_billing.Resources.Verifications.Operations import ListVerifications


class TestListVerifications:
    def test_returns_no_parameters_by_default(self):
        assert ListVerifications().get_parameters() == {}

    def test_returns_pager_parameters(self):
        assert ListVerifications(Pager()).get_parameters() == {"order_by": "id[asc]", "per_page": 50}

    def test_returns_id_and_type_parameters(self):
        operation = ListVerifications(ids=["slrvrf_1", "slrvrf_2"], verification_type=VerificationType.Domain)

        assert operation.get_parameters() == {"id": "slrvrf_1,slrvrf_2", "verification_type": "domain"}

    def test_raises_invalid_argument_exception_for_invalid_ids(self):
        with raises(InvalidArgumentException) as exception_info:
            ListVerifications(ids=[1])

        assert str(exception_info.value) == "Expected 'ids' to only contain type 'str' ('int' given)"
