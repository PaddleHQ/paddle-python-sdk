from pytest import mark, raises

from paddle_billing.Entities.CheckoutDomains import CheckoutDomainStatus

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.CheckoutDomains.Operations import ListCheckoutDomains
from paddle_billing.Resources.Shared.Operations import Pager


class TestListCheckoutDomains:
    def test_returns_no_parameters_by_default(self):
        operation = ListCheckoutDomains()

        assert operation.get_parameters() == {}

    def test_returns_pager_parameters(self):
        operation = ListCheckoutDomains(Pager())

        assert operation.get_parameters() == {"order_by": "id[asc]", "per_page": 50}

    def test_returns_domain_parameter(self):
        operation = ListCheckoutDomains(domain="example.com")

        assert operation.get_parameters() == {"domain": "example.com"}

    @mark.parametrize(
        "statuses, expected_status_parameter",
        [
            ([CheckoutDomainStatus.Approved], "approved"),
            (
                [CheckoutDomainStatus.Approved, CheckoutDomainStatus.PendingReview],
                "approved,pending_review",
            ),
        ],
        ids=[
            "Single status",
            "Multiple statuses",
        ],
    )
    def test_returns_status_parameter(self, statuses, expected_status_parameter):
        operation = ListCheckoutDomains(statuses=statuses)

        assert operation.get_parameters() == {"status": expected_status_parameter}

    def test_raises_invalid_argument_exception_for_invalid_statuses(self):
        with raises(InvalidArgumentException) as exception_info:
            ListCheckoutDomains(statuses=[1])

        assert (
            str(exception_info.value) == "Expected 'statuses' to only contain type 'CheckoutDomainStatus' ('int' given)"
        )
