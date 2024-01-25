from typing      import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.PriceWithIncludes import PriceWithIncludes

from paddle_billing_python_sdk.Entities.Collections.Paginator                   import Paginator
from paddle_billing_python_sdk.Entities.Collections.PriceWithIncludesCollection import PriceWithIncludesCollection

from paddle_billing_python_sdk.Entities.Shared.Status import Status

from paddle_billing_python_sdk.Resources.Prices.Operations.CreatePrice import CreatePrice
from paddle_billing_python_sdk.Resources.Prices.Operations.ListPrices  import ListPrices
from paddle_billing_python_sdk.Resources.Prices.Operations.UpdatePrice import UpdatePrice


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class PricesClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self, operation: ListPrices = None) -> PriceWithIncludesCollection:
        if operation is None:
            operation = ListPrices()

        response = self.client.get_raw('/prices', operation.get_parameters())
        parser   = ResponseParser(response)
        return PriceWithIncludesCollection.from_list(parser.get_data(), Paginator(self.client, parser.get_pagination(), PriceWithIncludesCollection))


    def get(self, price_id: str, includes = None) -> PriceWithIncludes:
        if includes is None:
            includes = []

        # Validate 'includes' items and build parameters
        parameters = {'include': ','.join(include.value for include in includes)} if includes else {}
        response   = self.client.get_raw(f"/prices/{price_id}", parameters)
        parser     = ResponseParser(response)

        return PriceWithIncludes.from_dict(parser.get_data())


    def create(self, operation: CreatePrice) -> PriceWithIncludes:
        response = self.client.post_raw('/prices', operation.get_parameters())
        parser   = ResponseParser(response)

        return PriceWithIncludes.from_dict(parser.get_data())


    def update(self, price_id: str, operation: UpdatePrice) -> PriceWithIncludes:
        response = self.client.patch_raw(f"/prices/{price_id}", operation.get_parameters())
        parser   = ResponseParser(response)

        return PriceWithIncludes.from_dict(parser.get_data())


    def archive(self, price_id: str) -> PriceWithIncludes:
        operation = UpdatePrice(status=Status.Archived)

        return self.update(price_id, operation)
