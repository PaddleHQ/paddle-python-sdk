from src.ResponseParser import ResponseParser

from src.Entities.PriceWithIncludes import PriceWithIncludes

from src.Entities.Collections.Paginator                   import Paginator
from src.Entities.Collections.PriceWithIncludesCollection import PriceWithIncludesCollection

from src.Entities.Shared.Status import Status

# from src.Resources.Prices.Operations.CreatePrice import CreatePrice
from src.Resources.Prices.Operations.ListPrices  import ListPrices
# from src.Resources.Prices.Operations.UpdatePrice import UpdatePrice


class PricesClient:
    def __init__(self, client):
        self.client = client


    def list(self, list_operation: ListPrices = None):
        if list_operation is None:
            list_operation = ListPrices()

        response = self.client.get_raw('/prices', list_operation.get_parameters())
        parser   = ResponseParser(response)
        return PriceWithIncludesCollection.from_list(parser.get_data(), Paginator(self.client, parser.get_pagination(), PriceWithIncludesCollection))


    def get(self, price_id: str, includes = None):
        if includes is None:
            includes = []

        # Validate 'includes' items and build parameters
        params   = {'include': ','.join(include.value for include in includes)} if includes else {}
        response = self.client.get_raw(f"/prices/{price_id}", params)
        parser   = ResponseParser(response)

        return PriceWithIncludes.from_dict(parser.get_data())


    # def create(self, create_operation: CreatePrice):
    #     response = self.client.post_raw('/prices', create_operation.get_parameters())
    #     parser   = ResponseParser(response)
    #
    #     return PriceWithIncludes.from_dict(parser.get_data())
    #
    #
    # def update(self, price_id: str, operation: UpdatePrice):
    #     response = self.client.patch_raw(f"/prices/{price_id}", operation.get_parameters())
    #     parser   = ResponseParser(response)
    #
    #     return PriceWithIncludes.from_dict(parser.get_data())
    #
    #
    # def archive(self, price_id: str):
    #     operation = UpdatePrice(status=Status.Archived)
    #
    #     return self.update(price_id, operation)
