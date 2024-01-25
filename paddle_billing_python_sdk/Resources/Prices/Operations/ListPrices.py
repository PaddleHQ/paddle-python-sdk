from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.Status      import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Prices.Operations.List.Includes import Includes


class ListPrices:
    def __init__(
        self, 
        pager             = None,
        includes:    dict = None,
        ids:         dict = None,
        types:       dict = None,
        product_ids: dict = None,
        statuses:    dict = None,
        recurring:   dict = None
    ):
        self.pager       = pager
        self.includes    = includes    if includes    is not None else []
        self.ids         = ids         if ids         is not None else []
        self.types       = types       if types       is not None else []
        self.product_ids = product_ids if product_ids is not None else []
        self.statuses    = statuses    if statuses    is not None else []
        self.recurring   = recurring

        # Validation
        if any(not isinstance(include, Includes) for include in self.includes):
            raise InvalidArgumentException('includes', Includes.__name__)
        if any(not isinstance(i, str) for i in self.ids):
            raise InvalidArgumentException('ids', 'string')
        if any(not isinstance(t, CatalogType) for t in self.types):
            raise InvalidArgumentException('types', CatalogType.__name__)
        if any(not isinstance(pid, str) for pid in self.product_ids):
            raise InvalidArgumentException('productIds', 'string')
        if any(not isinstance(status, Status) for status in self.statuses):
            raise InvalidArgumentException('statuses', Status.__name__)


    def get_parameters(self) -> dict:
        enum_stringify = lambda enum: enum.value  # noqa E731

        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.includes:
            parameters['include'] = ','.join(map(enum_stringify, self.includes))
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.types:
            parameters['type'] = ','.join(map(enum_stringify, self.types))
        if self.product_ids:
            parameters['product_id'] = ','.join(self.product_ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.recurring is not None:
            parameters['recurring'] = 'true' if self.recurring else 'false'

        return parameters
