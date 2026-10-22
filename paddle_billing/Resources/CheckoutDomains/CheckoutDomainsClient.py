from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import CheckoutDomainCollection, Paginator
from paddle_billing.Entities.CheckoutDomain import CheckoutDomain

from paddle_billing.Resources.CheckoutDomains.Operations import ListCheckoutDomains, VerifyCheckoutDomainPaymentMethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CheckoutDomainsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListCheckoutDomains | None = None) -> CheckoutDomainCollection:
        if operation is None:
            operation = ListCheckoutDomains()

        self.response = self.client.get_raw("/checkout-domains", operation.get_parameters())
        parser = ResponseParser(self.response)

        return CheckoutDomainCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), CheckoutDomainCollection)
        )

    def get(self, checkout_domain_id: str) -> CheckoutDomain:
        self.response = self.client.get_raw(f"/checkout-domains/{checkout_domain_id}")
        parser = ResponseParser(self.response)

        return CheckoutDomain.from_dict(parser.get_dict())

    def delete(self, checkout_domain_id: str) -> None:
        self.client.delete_raw(f"/checkout-domains/{checkout_domain_id}")

        return None

    def verify_payment_method(
        self, checkout_domain_id: str, operation: VerifyCheckoutDomainPaymentMethod
    ) -> CheckoutDomain:
        self.response = self.client.post_raw(f"/checkout-domains/{checkout_domain_id}/verify-payment-method", operation)
        parser = ResponseParser(self.response)

        return CheckoutDomain.from_dict(parser.get_dict())
